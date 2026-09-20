/**
 * Visitor counter for the homepage map widget.
 *
 * Why this exists: the map used to be ClustrMaps, which shut down in 2026
 * without notice and took every site's visitor history with it. Running the
 * counter yourself means the data sits in your own Cloudflare account and can
 * be exported at any time.
 *
 * One GET does everything:
 *   GET /            -> { total, countries: { US: 12, CN: 4, ... } }
 *   GET /?count=1    -> same, and records this visit first
 *
 * The visitor's country comes from `request.cf.country`, which Cloudflare
 * fills in at the edge, so there is no third-party geolocation call and no IP
 * address is ever stored — only a per-country tally.
 *
 * Budget: the free plan allows 100k KV reads and 1k KV writes per day. Reads
 * happen on every page view, writes only when the page asks to be counted,
 * which the widget does at most once per visitor per day.
 */

const KEY = 'stats';

/* Only this site may call the worker, so someone else cannot inflate it from
   their own page. Add origins here if the site moves. */
const ALLOWED = [
  'https://zhang-henry.github.io',
  'http://localhost:4001',
  'http://127.0.0.1:4001',
];

function cors(origin) {
  const allow = ALLOWED.includes(origin) ? origin : ALLOWED[0];
  return {
    'Access-Control-Allow-Origin': allow,
    'Access-Control-Allow-Methods': 'GET, OPTIONS',
    'Vary': 'Origin',
    'Cache-Control': 'no-store',
    'Content-Type': 'application/json; charset=utf-8',
  };
}

export default {
  async fetch(request, env) {
    const origin = request.headers.get('Origin') || '';
    const headers = cors(origin);

    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers });
    }
    if (request.method !== 'GET') {
      return new Response('{"error":"method not allowed"}', { status: 405, headers });
    }

    const url = new URL(request.url);
    const shouldCount = url.searchParams.get('count') === '1';

    let stats = (await env.VISITS.get(KEY, { type: 'json' })) || { total: 0, countries: {} };
    if (!stats.countries) { stats.countries = {}; }

    if (shouldCount && ALLOWED.includes(origin)) {
      const cc = (request.cf && request.cf.country) || 'XX';
      stats.total = (stats.total || 0) + 1;
      stats.countries[cc] = (stats.countries[cc] || 0) + 1;
      stats.updated = new Date().toISOString();
      // Not awaited: the response does not need to wait on the write.
      await env.VISITS.put(KEY, JSON.stringify(stats));
    }

    return new Response(JSON.stringify({
      total: stats.total || 0,
      countries: stats.countries,
      updated: stats.updated || null,
    }), { headers });
  },
};
