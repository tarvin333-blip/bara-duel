"""Pack web/art/cg/*.png into two JSON bundles (story / love) so the published artifact stays under its file-count limit."""
import base64, glob, json, os
st, lv = {}, {}
for f in sorted(glob.glob('../web/art/cg/*.png')):
    n = os.path.basename(f)
    (st if n.startswith('st_') else lv)[n] = 'data:image/png;base64,' + base64.b64encode(open(f, 'rb').read()).decode()
json.dump(st, open('../web/art/cg_story.json', 'w'), separators=(',', ':'))
json.dump(lv, open('../web/art/cg_love.json', 'w'), separators=(',', ':'))
print(len(st), 'story,', len(lv), 'love')
