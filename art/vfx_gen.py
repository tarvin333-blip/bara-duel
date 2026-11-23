"""PixelLab VFX helper: python3 vfx_gen.py <name> "<description>" [sprite.png] [--pro]
Saves art/vfxgen/<name>.{png,json,gif} (+ -game.zip with a sprite) and prints the cost. Key comes from the proxy."""
import json, os, sys, time, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pl
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vfxgen')
def fetch(url, path):
    req = urllib.request.Request(url, headers={'User-Agent': 'curl/8'})
    open(path, 'wb').write(urllib.request.urlopen(req, timeout=120).read())
def make(name, desc, sprite=None, artist='lite'):
    body = {'description': desc, 'artist': artist, 'name': 'bd_' + name}
    if sprite: body['sprite'] = pl.b64(sprite); body['game_pack'] = True
    before = pl.gens()
    r = pl.call('POST', '/vfx', body)
    if 'http_error' in r: print('ERROR', r); return None
    job = r.get('background_job_id'); print(name, 'quote', r.get('quoted_generations'), 'job', job, flush=True)
    while True:
        time.sleep(8)
        j = pl.call('GET', f'/background-jobs/{job}')
        if j.get('status') in ('completed', 'failed', 'error', 'cancelled'): break
    if j.get('status') != 'completed': print('JOB', json.dumps(j)[:800]); return None
    lr = j['last_response']; files = lr.get('files') or {}
    meta = {k: lr.get(k) for k in ('effect_id', 'canvas', 'frames', 'fps', 'loop', 'anchor', 'message')}
    json.dump({'meta': meta, 'files': files}, open(f'{OUT}/{name}.meta.json', 'w'), ensure_ascii=False, indent=1)
    items = files.items() if isinstance(files, dict) else [(f.get('name', str(i)), f.get('url')) for i, f in enumerate(files)]
    for fname, url in items:
        if isinstance(url, dict): url = url.get('url')
        if not url: continue
        ext = fname.split('.')[-1] if '.' in fname else 'bin'
        tag = 'game.zip' if fname.endswith('.zip') else ('normals.png' if 'normals' in fname else ext)
        fetch(url, f'{OUT}/{name}.{tag}')
    time.sleep(2); print(name, 'done; gens used', round(before - pl.gens(), 2), '| canvas', meta['canvas'], 'frames', meta['frames'], 'fps', meta['fps'], '| anchor', meta['anchor'])
    print('  artist:', (meta.get('message') or '')[:300])
    return meta
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if x != '--pro']
    make(a[0], a[1], a[2] if len(a) > 2 else None, 'pro' if '--pro' in sys.argv else 'lite')
