#!/usr/bin/env python3
"""Fetch Google Scholar stats using nothing but the standard library.

The scholarly-based crawler needs 56 packages to parse one HTML page, and twice
in a week an unpinned upstream release broke it before it made a single request
(free-proxy's API change, then bibtexparser 2.0 dropping a module scholarly
imports). Nothing here can break that way.

Writes results/gs_data.json and results/gs_data_shieldsio.json in the same shape
the site already reads.

  --probe   report whether Scholar answers, and write nothing
"""

import argparse
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime

PROFILE = "https://scholar.google.com/citations?user={uid}&hl=en&pagesize=100&cstart={start}"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

ATTEMPTS = 5
RETRY_WAIT = 60


class Blocked(Exception):
    pass


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            body = r.read().decode("utf-8", errors="replace")
            status = r.status
    except urllib.error.HTTPError as e:
        raise Blocked(f"HTTP {e.code}") from e
    if re.search(r"captcha|unusual traffic|not a robot", body, re.I):
        raise Blocked(f"HTTP {status}, {len(body)} bytes, captcha/block page")
    return status, body


def parse_indices(page):
    nums = [int(n) for n in re.findall(r'gsc_rsb_std">(\d+)</td>', page)]
    keys = ["citedby", "citedby5y", "hindex", "hindex5y", "i10index", "i10index5y"]
    return dict(zip(keys, nums))


def parse_cites_per_year(page):
    years = re.findall(r'class="gsc_g_t"[^>]*>(\d{4})</span>', page)
    counts = re.findall(r'class="gsc_g_al"[^>]*>(\d+)</span>', page)
    # Zero-height bars are omitted from the markup, so only trust the pairing
    # when both lists line up.
    return {y: int(c) for y, c in zip(years, counts)} if len(years) == len(counts) else {}


def parse_publications(page):
    pubs = {}
    for row in re.findall(r'<tr class="gsc_a_tr">(.*?)</tr>', page, re.S):
        m = re.search(r'citation_for_view=([^"&]+)"[^>]*>(.*?)</a>', row, re.S)
        if not m:
            continue
        cites = re.search(r'class="gsc_a_ac[^"]*"[^>]*>(\d*)</a>', row)
        year = re.search(r'class="gsc_a_h[^"]*"[^>]*>(\d{4})</span>', row)
        pubs[m.group(1)] = {
            "author_pub_id": m.group(1),
            "num_citations": int(cites.group(1)) if cites and cites.group(1) else 0,
            "bib": {
                "title": html.unescape(re.sub(r"<[^>]+>", "", m.group(2))).strip(),
                "pub_year": year.group(1) if year else "",
            },
        }
    return pubs


def scrape(uid, verbose=False):
    status, page = get(PROFILE.format(uid=uid, start=0))
    if verbose:
        print(f"  HTTP {status}, {len(page)} bytes")

    indices = parse_indices(page)
    if "citedby" not in indices:
        raise Blocked("citation table missing - blocked, or Scholar changed its markup")

    pubs = parse_publications(page)
    # The profile pages 100 at a time; keep going while a page comes back full.
    start = len(pubs)
    while start and start % 100 == 0:
        more = parse_publications(get(PROFILE.format(uid=uid, start=start))[1])
        if not more:
            break
        pubs.update(more)
        start += len(more)
    if not pubs:
        raise Blocked("no publications parsed")

    name = re.search(r'id="gsc_prf_in">(.*?)</div>', page)
    return {
        "scholar_id": uid,
        "name": html.unescape(re.sub(r"<[^>]+>", "", name.group(1))).strip() if name else "",
        "cites_per_year": parse_cites_per_year(page),
        "publications": pubs,
        "updated": str(datetime.now()),
        **indices,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--probe", action="store_true")
    args = ap.parse_args()

    uid = os.environ["GOOGLE_SCHOLAR_ID"]

    data = None
    for attempt in range(1, ATTEMPTS + 1):
        try:
            data = scrape(uid, verbose=True)
            break
        except (Blocked, urllib.error.URLError, TimeoutError) as exc:
            print(f"Attempt {attempt}/{ATTEMPTS} failed: {type(exc).__name__}: {exc}", flush=True)
            if attempt < ATTEMPTS:
                print(f"Waiting {RETRY_WAIT}s before retrying...", flush=True)
                time.sleep(RETRY_WAIT)

    if data is None:
        sys.exit(f"Could not fetch Scholar data after {ATTEMPTS} attempts.")

    print("Done. %d publications, %d citations, h-index %s, i10 %s."
          % (len(data["publications"]), data["citedby"], data["hindex"], data["i10index"]))

    if args.probe:
        print("PROBE OK - Scholar answered a direct request from this host.")
        return

    os.makedirs("results", exist_ok=True)
    with open("results/gs_data.json", "w") as f:
        json.dump(data, f, ensure_ascii=False)
    with open("results/gs_data_shieldsio.json", "w") as f:
        json.dump({"schemaVersion": 1, "label": "citations",
                   "message": str(data["citedby"])}, f, ensure_ascii=False)


if __name__ == "__main__":
    main()
