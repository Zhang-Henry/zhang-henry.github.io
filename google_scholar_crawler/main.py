from scholarly import scholarly, ProxyGenerator
import json
import os
import sys
import time
from datetime import datetime

SCHOLAR_ID = os.environ["GOOGLE_SCHOLAR_ID"]

# Scholar throttles bursts, so a failed attempt is retried after a pause rather
# than immediately.
ATTEMPTS = 5
RETRY_WAIT = 60

# Scholar sometimes lists one paper as several entries (preprint vs. published
# version, retitled arXiv versions) and splits its citations across them. The
# site shows each paper's combined count, so the duplicates' citations are
# folded into the entry the site links to. Total citations and h-index are kept
# exactly as Scholar reports them. Add new pairs here when Scholar splits again.
MERGE_INTO = {
    # LLM-Based Human-Agent survey (ACL 2026) <- TechRxiv version
    "qG5_O40AAAAJ:maZDTaKrznsC": ["qG5_O40AAAAJ:OU6Ihb5iCvQC"],
    # Agent Memory survey (TMLR) <- arXiv 2602.06052 "Rethinking memory mechanisms..."
    "qG5_O40AAAAJ:f2IySw72cVMC": ["qG5_O40AAAAJ:u9iWguZQMMsC", "qG5_O40AAAAJ:p2g8aNsByqUC"],
    # Class-incremental fault diagnosis (TII) <- SCLIFD arXiv preprint
    "qG5_O40AAAAJ:4DMP91E08xMC": ["qG5_O40AAAAJ:D03iK_w7-QYC"],
    # GAM (ACL 2026) <- ICLR 2026 workshop version
    "qG5_O40AAAAJ:fPk4N6BV_jEC": ["qG5_O40AAAAJ:u_35RYKgDlwC"],
}


def merge_duplicates(publications):
    for primary, dups in MERGE_INTO.items():
        if primary not in publications:
            continue
        found = [d for d in dups if d in publications]
        extra = sum(publications[d].get("num_citations") or 0 for d in found)
        publications[primary]["num_citations"] = (publications[primary].get("num_citations") or 0) + extra
        publications[primary]["merged_from"] = found


def fetch_author():
    # SCHOLAR_NO_PROXY=1 fetches directly, for running this from a personal
    # machine when Scholar blocks the free proxies used on GitHub's runners.
    if os.environ.get("SCHOLAR_NO_PROXY") != "1":
        pg = ProxyGenerator()
        pg.FreeProxies()
        scholarly.use_proxy(pg)

    author = scholarly.search_author_id(SCHOLAR_ID)
    # This is the only Scholar request we need. The publication list on the
    # profile page already carries num_citations and author_pub_id for every
    # paper -- which is all the site renders -- so we deliberately do NOT call
    # scholarly.fill() on each publication. That used to fire one extra request
    # per paper (30+ per run); Scholar cut the burst off partway through and the
    # parser then died on a page it could not read.
    scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])
    return author


author = None
for attempt in range(1, ATTEMPTS + 1):
    try:
        author = fetch_author()
        break
    except Exception as exc:
        print(f"Attempt {attempt}/{ATTEMPTS} failed: {type(exc).__name__}: {exc}", flush=True)
        if attempt < ATTEMPTS:
            print(f"Waiting {RETRY_WAIT}s before retrying...", flush=True)
            time.sleep(RETRY_WAIT)

if author is None:
    # Exit non-zero so the run shows up as failed. Previously this path printed
    # the error and exited 0, so the workflow went green while writing nothing
    # and the published stats silently went stale.
    sys.exit(f"Could not fetch Scholar data after {ATTEMPTS} attempts.")

publications = {p["author_pub_id"]: p for p in author["publications"]}
if not publications or "citedby" not in author:
    sys.exit("Fetched data looks incomplete; refusing to overwrite the published stats.")

merge_duplicates(publications)
author["publications"] = publications
author["updated"] = str(datetime.now())

os.makedirs("results", exist_ok=True)

with open("results/gs_data.json", "w") as outfile:
    json.dump(author, outfile, ensure_ascii=False)

with open("results/gs_data_shieldsio.json", "w") as outfile:
    json.dump({
        "schemaVersion": 1,
        "label": "citations",
        "message": f"{author.get('citedby', 0)}",
    }, outfile, ensure_ascii=False)

print(
    f"Done. {len(publications)} publications, {author['citedby']} citations, "
    f"h-index {author.get('hindex')}, i10 {author.get('i10index')}."
)
