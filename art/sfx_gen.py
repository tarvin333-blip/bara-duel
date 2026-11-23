"""PixelLab sound helper: python3 sfx_gen.py <name> <seconds> "<prompt>"   -> art/sfx/<name>.wav (+ web/audio/<name>.mp3)
Music:                 python3 sfx_gen.py --music <name> <length_s> "<style>" -> art/sfx/<name>_{1,2}.mp3
The PixelLab key is injected by the session proxy."""
import json, os, sys, time, subprocess, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pl
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, 'sfx'); WEB = os.path.join(ROOT, '..', 'web', 'audio')
os.makedirs(OUT, exist_ok=True); os.makedirs(WEB, exist_ok=True)
def fetch(url, path):
    open(path, 'wb').write(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'curl/8'}), timeout=180).read())
def mp3(src, dst, br='96k'):
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', src, '-ac', '1', '-b:a', br, dst], check=True)
def sfx(name, secs, prompt):
    r = pl.call('POST', '/sound-effects', {'prompt': prompt, 'seconds': float(secs), 'name': 'bd_' + name})
    if 'http_error' in r: print(name, 'ERROR', r); return
    sid = r.get('id') or r.get('sound_effect_id') or (r.get('sound_effect') or {}).get('id'); job = r.get('background_job_id')
    for _ in range(60):
        time.sleep(4)
        j = pl.call('GET', f'/sound-effects/{sid}') if sid else pl.call('GET', f'/background-jobs/{job}')
        jj = j.get('sound_effect', j) if isinstance(j, dict) else {}
        url = jj.get('audio_url') or (jj.get('last_response') or {}).get('audio_url')
        st = jj.get('status')
        if url: break
        if st in ('failed', 'error'): print(name, 'FAILED', json.dumps(j)[:300]); return
    else: print(name, 'TIMEOUT'); return
    wav = f'{OUT}/{name}.wav'; fetch(url, wav); mp3(wav, f'{WEB}/{name}.mp3')
    print(name, 'ok', jj.get('duration_ms'), 'ms quote', r.get('quoted_generations'))
def music(name, length, style):
    r = pl.call('POST', '/music', {'style': style, 'instrumental': True, 'length_s': int(length), 'name': 'bd_' + name})
    if 'http_error' in r: print(name, 'ERROR', r); return
    ids = r.get('song_ids') or [r.get('id') or (r.get('song') or {}).get('id')]
    print(name, 'submitted', json.dumps(r)[:300], flush=True)
    for k, sid in enumerate([i for i in ids if i]):
        for _ in range(40):
            time.sleep(10)
            j = pl.call('GET', f'/music/{sid}'); jj = j.get('song', j)
            if jj.get('audio_url'): break
            if jj.get('status') in ('failed', 'error'): print(name, 'FAILED', json.dumps(j)[:300]); break
        if jj.get('audio_url'):
            src = f'{OUT}/{name}_{k + 1}.mp3'; fetch(jj['audio_url'], src); subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', src, '-b:a', '112k', f'{WEB}/{name}_{k + 1}.mp3'], check=True)
            print(name, 'take', k + 1, 'ok', jj.get('duration_ms'), 'id', sid)
if __name__ == '__main__':
    if sys.argv[1] == '--music': music(sys.argv[2], sys.argv[3], sys.argv[4])
    else: sfx(sys.argv[1], sys.argv[2], sys.argv[3])
