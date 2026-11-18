"""Tiny PixelLab v2 helper: python3 pl.py <endpoint> <request.json> <out_prefix>  (key from PIXELLAB_KEY)"""
import base64, json, os, sys, time, urllib.request
API = 'https://api.pixellab.ai/v2'
KEY = os.environ.get('PIXELLAB_KEY', '')
def call(method, path, body=None):
    req = urllib.request.Request(API + path, method=method, data=json.dumps(body).encode() if body is not None else None,
                                 headers={'Authorization': 'Bearer ' + KEY, 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=120) as r: return json.loads(r.read())
    except urllib.error.HTTPError as e: return {'http_error': e.code, 'body': e.read().decode()[:2000]}
def b64(path): return {'type': 'base64', 'base64': base64.b64encode(open(path, 'rb').read()).decode(), 'format': 'png'}
def gens(): return call('GET', '/balance')['subscription']['generations']
def find_images(o, acc):
    if isinstance(o, dict):
        if 'base64' in o and isinstance(o['base64'], str) and len(o['base64']) > 100: acc.append(o['base64'])
        for v in o.values(): find_images(v, acc)
    elif isinstance(o, list):
        for v in o: find_images(v, acc)
    return acc
if __name__ == '__main__':
    ep, reqf, out = sys.argv[1:4]
    body = json.load(open(reqf))
    before = gens()
    r = call('POST', ep, body)
    if 'http_error' in r: print('ERROR', r); sys.exit(1)
    job = r.get('background_job_id')
    while job:
        time.sleep(6)
        j = call('GET', f'/background-jobs/{job}')
        st = j.get('status')
        if st in ('completed', 'failed', 'error', 'cancelled'): r = j; break
    if r.get('status') not in (None, 'completed'): print('JOB', json.dumps(r)[:1500]); sys.exit(1)
    imgs = find_images(r, [])
    for i, s in enumerate(imgs): open(f'{out}_{i}.png', 'wb').write(base64.b64decode(s))
    time.sleep(2); after = gens()
    meta = {k: v for k, v in (r.get('last_response') or r).items() if not isinstance(v, (dict, list)) or k in ('usage',)}
    print(json.dumps({'images': len(imgs), 'gens_used': round(before - after, 3), 'left': after, 'meta': str(meta)[:400]}))
