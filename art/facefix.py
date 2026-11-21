import json, subprocess, sys, re, os
sys.path.insert(0,'.'); from pl import b64
src=open('build_art.py').read()
ids=sys.argv[1:]
FIX=("redraw only his head and face: a handsome rugged masculine face, both eyes clearly visible with defined pupils looking forward, "
     "a closed-mouth confident smile with no missing teeth, no fangs, no face paint, natural skin tone without red cheeks, clean detailed pixel shading, strong jaw and neat beard; "
     "keep exactly the same hair, headwear, beard color, body, pose, outfit, accessories and colors")
for cid in ids:
  m=re.search(r"'%s':\s*\(([^)]*)\)"%cid,src); files=[f.strip().strip("'") for f in m.group(1).split(',') if f.strip()]
  for f in dict.fromkeys(files):
    base=f[:-6]; out=base+'F'
    req=f'/tmp/claude-0/ff_{os.path.basename(base)}.json'
    json.dump({"image": b64(f), "description": FIX, "no_background": True}, open(req,'w'))
    r=subprocess.run(['python3','pl.py','/edit-image-pixen',req,out],capture_output=True,text=True); print(os.path.basename(out), r.stdout[:50], flush=True)
