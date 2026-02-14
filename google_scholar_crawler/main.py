from scholarly import scholarly, ProxyGenerator
import json
from datetime import datetime
import os
import sys
import time


def fetch_with_free_proxy(scholar_id):
    """Try fetching with free proxy."""
    pg = ProxyGenerator()
    pg.FreeProxies()
    scholarly.use_proxy(pg)
    author = scholarly.search_author_id(scholar_id)
    scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
    return author


def fetch_without_proxy(scholar_id):
    """Try fetching directly without proxy."""
    scholarly.use_proxy(None)
    author = scholarly.search_author_id(scholar_id)
    scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
    return author


def load_previous_data():
    """Load previous citation data as fallback."""
    for path in ['results/gs_data.json', '../google-scholar-stats/gs_data.json']:
        try:
            with open(path, 'r') as f:
                data = json.load(f)
                if data.get('citedby'):
                    print(f"Loaded previous data from {path}: {data['citedby']} citations")
                    return data
        except (FileNotFoundError, json.JSONDecodeError):
            continue
    return None


def save_results(author_data):
    """Save citation data to JSON files."""
    os.makedirs('results', exist_ok=True)

    # Build publications dict with short keys
    publications = {}
    for pub in author_data.get('publications', []):
        pub_id = pub.get('author_pub_id', '')
        # Use the short key (part after the colon) if available
        short_key = pub_id.split(':')[-1] if ':' in pub_id else pub_id
        publications[short_key] = {
            'title': pub.get('bib', {}).get('title', ''),
            'num_citations': pub.get('num_citations', 0),
        }

    gs_data = {
        'citedby': author_data.get('citedby', 0),
        'name': author_data.get('name', ''),
        'updated': str(datetime.now()),
        'publications': publications,
    }

    with open('results/gs_data.json', 'w') as f:
        json.dump(gs_data, f, ensure_ascii=False, indent=2)

    shieldio_data = {
        'schemaVersion': 1,
        'label': 'citations',
        'message': str(gs_data['citedby']),
    }

    with open('results/gs_data_shieldsio.json', 'w') as f:
        json.dump(shieldio_data, f, ensure_ascii=False, indent=2)

    print(f"Saved results: {gs_data['citedby']} total citations, {len(publications)} publications")
    return gs_data


def main():
    scholar_id = os.environ.get('GOOGLE_SCHOLAR_ID', 'qG5_O40AAAAJ')
    print(f"Google Scholar ID: {scholar_id}")

    # Try multiple strategies
    strategies = [
        ("without proxy", fetch_without_proxy),
        ("with free proxy", fetch_with_free_proxy),
    ]

    for name, fetch_fn in strategies:
        for attempt in range(2):
            try:
                print(f"Strategy: {name}, attempt {attempt + 1}")
                author = fetch_fn(scholar_id)
                if author and author.get('citedby', 0) > 0:
                    print(f"Success! {author['name']}: {author['citedby']} citations")
                    save_results(author)
                    return
            except Exception as e:
                print(f"Failed: {e}")
                time.sleep(5 * (attempt + 1))

    # All strategies failed — use previous data
    print("All fetch strategies failed. Trying previous data as fallback.")
    prev = load_previous_data()
    if prev:
        os.makedirs('results', exist_ok=True)
        prev['updated'] = str(datetime.now()) + ' (fallback)'
        with open('results/gs_data.json', 'w') as f:
            json.dump(prev, f, ensure_ascii=False, indent=2)
        shieldio_data = {
            'schemaVersion': 1,
            'label': 'citations',
            'message': str(prev['citedby']),
        }
        with open('results/gs_data_shieldsio.json', 'w') as f:
            json.dump(shieldio_data, f, ensure_ascii=False, indent=2)
        print(f"Used fallback: {prev['citedby']} citations")
    else:
        print("No previous data available either.")
        sys.exit(1)


if __name__ == '__main__':
    main()
