#!/usr/bin/env python3
"""
Google Scholar Citations Updater
Fetches citation counts from Google Scholar and updates the gs_data.json file
"""

import json
import os
import requests
from bs4 import BeautifulSoup
import time
import re


def get_citation_count_from_scholar(paper_title, author_name="Hanrong Zhang"):
    """
    Get citation count for a paper from Google Scholar
    """
    # Clean title for search
    clean_title = re.sub(r'[^\w\s]', '', paper_title).strip()
    query = f'"{clean_title}" "{author_name}"'
    
    # Google Scholar search URL
    url = f"https://scholar.google.com/scholar?q={query.replace(' ', '+')}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find citation links
        citation_links = soup.find_all('a', href=re.compile(r'scholar\?cites='))
        
        if citation_links:
            # Extract number from "Cited by X" text
            citation_text = citation_links[0].text
            match = re.search(r'Cited by (\d+)', citation_text)
            if match:
                return int(match.group(1))
        
        return 0
    except Exception as e:
        print(f"Error fetching citation for '{paper_title}': {e}")
        return 0


def main():
    # Paper data with Scholar-specific identifiers or titles
    papers = {
        "ASB": {
            "title": "Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents",
            "num_citations": 0
        },
        "INACTIVE": {
            "title": "Invisible Backdoor Attack in Self-supervised Learning", 
            "num_citations": 0
        },
        "SCLIFD": {
            "title": "Class Incremental Fault Diagnosis under Limited Fault Data via Supervised Contrastive Knowledge Distillation",
            "num_citations": 0
        },
        "GOOFD": {
            "title": "Generalized Out-of-distribution Fault Diagnosis via Internal Contrastive Learning",
            "num_citations": 0
        },
        "BGAN": {
            "title": "Imbalanced Chemical Process Fault Diagnosis Using Balancing GAN With Active Sample Selection",
            "num_citations": 0
        }
    }
    
    print("Fetching citation counts from Google Scholar...")
    
    total_citations = 0
    for paper_id, paper_info in papers.items():
        print(f"Fetching citations for: {paper_info['title'][:50]}...")
        
        # Get citation count
        citations = get_citation_count_from_scholar(paper_info['title'])
        papers[paper_id]['num_citations'] = citations
        total_citations += citations
        
        print(f"  -> {citations} citations")
        
        # Be respectful to Google Scholar
        time.sleep(2)
    
    # Create the data structure expected by the Jekyll template
    data = {
        "citedby": total_citations,
        "publications": papers
    }
    
    # Create directory if it doesn't exist
    os.makedirs("google-scholar-stats", exist_ok=True)
    
    # Write the JSON file
    with open("google-scholar-stats/gs_data.json", "w") as f:
        json.dump(data, f, indent=2)
    
    # Also create the shields.io format
    shields_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(total_citations),
        "color": "brightgreen"
    }
    
    with open("google-scholar-stats/gs_data_shieldsio.json", "w") as f:
        json.dump(shields_data, f, indent=2)
    
    print(f"\nUpdated citation data:")
    print(f"Total citations: {total_citations}")
    print("Files updated:")
    print("- google-scholar-stats/gs_data.json")
    print("- google-scholar-stats/gs_data_shieldsio.json")


if __name__ == "__main__":
    main()