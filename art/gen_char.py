"""Generate a character's stages from a spec: python3 gen_char.py specs/<id>.json  (PIXELLAB_KEY in env)
spec = {"id":..., "base": "<prompt>", "stages": [["A1","A","<edit>"], ["B","A1","<edit>"]]}"""
import json, subprocess, sys, os
os.chdir(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, '.')
from pl import b64
TAIL = (", realistic adult proportions, about 8 heads tall, small head, not chibi, not cartoon, no big head, "
        "detailed 16-bit fighting game pixel art, bold dark outline, warm skin shading")
KEEP = ", do not touch his hands or what they hold, keep exact same pose, body shape, proportions, face and hair"
spec = json.load(open(sys.argv[1])); cid = spec['id']; tmp = '/tmp/claude-0/' + cid
req = tmp + '_A.json'
json.dump({"description": spec['base'] + TAIL, "image_size": {"width": 128, "height": 180}, "no_background": True,
           "style_image": {"image": b64('refs/ref1_tall.png'), "size": {"width": 128, "height": 180},
                           "usage_description": "match this sprite's pixel art style, outline and skin shading, but follow the described body type and pose"}}, open(req, 'w'))
r = subprocess.run(['python3', 'pl.py', '/create-image-pro-flash', req, f'chars/{cid}_A'], capture_output=True, text=True); print(cid, 'A', r.stdout[:60])
for st, src, desc in spec['stages']:
    req = f'{tmp}_{st}.json'
    json.dump({"image": b64(f'chars/{cid}_{src}_0.png'), "description": desc + KEEP, "no_background": True}, open(req, 'w'))
    r = subprocess.run(['python3', 'pl.py', '/edit-image-pixen', req, f'chars/{cid}_{st}'], capture_output=True, text=True); print(cid, st, r.stdout[:60], r.stderr[-120:])
