# Visitor counter

Backend for the visitor map at the bottom of the homepage. Runs on Cloudflare
Workers so the counts live in your own account and can be exported, rather than
on someone else's server — the previous widget was ClustrMaps, which shut down
in 2026 and took every site's history with it.

## Free-tier budget

| Resource   | Free allowance | What the widget uses                |
| ---------- | -------------- | ----------------------------------- |
| Requests   | 100,000 / day  | 1 per page view                     |
| KV reads   | 100,000 / day  | 1 per page view                     |
| KV writes  | 1,000 / day    | 1 per visitor per day               |
| Storage    | 1 GB           | a few hundred bytes                 |

Writes are the binding limit, so this supports roughly 1,000 new visitors a
day.

## Deploy

One-time, about five minutes. Needs a free Cloudflare account.

```bash
npm install -g wrangler
wrangler login
```

Create the KV namespace and note the id it prints:

```bash
wrangler kv namespace create VISITS
```

Put that id into `wrangler.toml` (replace `PUT_YOUR_KV_NAMESPACE_ID_HERE`),
then deploy:

```bash
cd visitor-counter
wrangler deploy
```

Wrangler prints a URL like `https://visitor-counter.<subdomain>.workers.dev`.

## Point the widget at it

In `_pages/about.md`:

```liquid
{% include visitor-map.html endpoint="https://visitor-counter.<subdomain>.workers.dev" %}
```

With no `endpoint` the widget falls back to a free keyless counter service,
which works without any setup but stores the data on a third party.

## Your data

Read the raw counts at any time:

```bash
wrangler kv key get --binding VISITS stats --remote
```

That returns the whole JSON blob — total, per-country tallies, last update —
which is the entire dataset. Back it up by redirecting it to a file.
