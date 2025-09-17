from scholarly import scholarly
import jsonpickle
import json
from datetime import datetime
import os
import time
import sys

def fetch_scholar_data_with_retry(scholar_id, max_retries=3):
    """Fetch Google Scholar data with retry mechanism"""
    for attempt in range(max_retries):
        try:
            print(f"Attempt {attempt + 1} to fetch data for Scholar ID: {scholar_id}")
            
            # Configure scholarly with some protective measures
            from scholarly import ProxyGenerator
            pg = ProxyGenerator()
            pg.FreeProxies()
            scholarly.use_proxy(pg)
            
            # Search for author
            author = scholarly.search_author_id(scholar_id)
            if not author:
                raise Exception("Author not found")
            
            # Fill author data
            scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
            print(f"Successfully fetched data for: {author.get('name', 'Unknown')}")
            return author
            
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {str(e)}")
            if attempt < max_retries - 1:
                wait_time = (attempt + 1) * 10  # Exponential backoff
                print(f"Waiting {wait_time} seconds before retry...")
                time.sleep(wait_time)
            else:
                print("All attempts failed. Using fallback data.")
                return None

# Get Scholar ID from environment or use default
scholar_id = os.environ.get('GOOGLE_SCHOLAR_ID', 'qG5_O40AAAAJ')
print(f"Using Google Scholar ID: {scholar_id}")

try:
    # Try to fetch data
    author = fetch_scholar_data_with_retry(scholar_id)
    
    if author:
        name = author['name']
        author['updated'] = str(datetime.now())
        author['publications'] = {v['author_pub_id']:v for v in author['publications']}
        
        # Create results directory
        os.makedirs('results', exist_ok=True)
        
        # Save full data
        with open(f'results/gs_data.json', 'w') as outfile:
            json.dump(author, outfile, ensure_ascii=False)
        
        # Create shields.io data
        shieldio_data = {
            "schemaVersion": 1,
            "label": "citations",
            "message": f"{author['citedby']}",
        }
        with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
            json.dump(shieldio_data, outfile, ensure_ascii=False)
        
        print(f"Successfully updated citation data. Total citations: {author['citedby']}")
        
    else:
        # Fallback: create minimal data structure
        print("Creating fallback data structure...")
        
        fallback_data = {
            "name": "Hanrong Zhang",
            "citedby": 77,  # Use last known count
            "updated": str(datetime.now()),
            "publications": {}
        }
        
        os.makedirs('results', exist_ok=True)
        
        with open(f'results/gs_data.json', 'w') as outfile:
            json.dump(fallback_data, outfile, ensure_ascii=False)
        
        shieldio_data = {
            "schemaVersion": 1,
            "label": "citations", 
            "message": "77",
        }
        with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
            json.dump(shieldio_data, outfile, ensure_ascii=False)
        
        print("Created fallback data files")

except Exception as e:
    print(f"Critical error: {str(e)}")
    sys.exit(1)
