"""Turn generated stages into game layers: web/art/<id>_{A,A1,B,c1,c0}.png + web/art/art.json (bounce regions, card placement)."""
import json
import numpy as np
from PIL import Image
# id: (full outfit, outer layer gone, bare). Characters with one clothing layer reuse A for A1.
CHARS = {
  'ben':    ('pilot/ben2_flash_0.png', 'pilot/ben2_A1_0.png', 'pilot/ben2_B_0.png'),
  'jompon': ('chars/jompon_A_0.png', 'chars/jompon_A1b_0.png', 'chars/jompon_B_0.png'),
  'dave':   ('chars/dave_A_0.png', 'chars/dave_A1_0.png', 'chars/dave_B2_0.png'),
  'champ':  ('chars/champ_A_0.png', 'chars/champ_A_0.png', 'chars/champ_B_0.png'),
  'ton':    ('chars/ton_A_0.png', 'chars/ton_A_0.png', 'chars/ton_B_0.png'),
  'ming':   ('chars/ming_A_0.png', 'chars/ming_A_0.png', 'chars/ming_B_0.png'),
  'jay':    ('chars/jay_A2_0.png', 'chars/jay_A2_0.png', 'chars/jay_B_0.png'),
  'dan':    ('chars/dan_A_0.png', 'chars/dan_A1_0.png', 'chars/dan_B5_0.png'),
  'fah':    ('chars/fah_A_0.png', 'chars/fah_A_0.png', 'chars/fah_B2_0.png'),
  'q':      ('chars/q_A_0.png', 'chars/q_A_0.png', 'chars/q_B_0.png'),
  'tiger':  ('chars/tiger_A_0.png', 'chars/tiger_A_0.png', 'chars/tiger_B_0.png'),
  'non':    ('chars/non_A_0.png', 'chars/non_A_0.png', 'chars/non_B_0.png'),
  'wchain': ('chars/wchain_A_0.png', 'chars/wchain_A1_0.png', 'chars/wchain_B_0.png'),
  'wneedle': ('chars/wneedle_A_0.png', 'chars/wneedle_A1_0.png', 'chars/wneedle_B_0.png'),
  'wchub': ('chars/wchub_A_0.png', 'chars/wchub_A1f_0.png', 'chars/wchub_Bf_0.png'),
  'wsumo': ('chars/wsumo_A_0.png', 'chars/wsumo_A1_0.png', 'chars/wsumo_B_0.png'),
  'wbutler': ('chars/wbutler_A_0.png', 'chars/wbutler_A1f_0.png', 'chars/wbutler_Bf_0.png'),
  'wgorilla': ('chars/wgorilla_A_0.png', 'chars/wgorilla_A1f_0.png', 'chars/wgorilla_Bf_0.png'),
  # 3-layer boss: (A3 full, A two layers, A1 one layer, B bare)
  'hunter': ('chars/hunter_A_0.png', 'chars/hunter_A2_0.png', 'chars/hunter_A1c_0.png', 'chars/hunter_Bc_0.png'),
}
REAR = {'ming', 'jay'}   # back-turned poses: the soft-body region is the butt, not the belly
def load(p): return np.array(Image.open(p).convert('RGBA')).astype(int)
def diff(top, under):
    d = np.abs(top[:, :, :3] - under[:, :, :3]).sum(2)
    m = (top[:, :, 3] > 0) & ((d > 60) | (under[:, :, 3] == 0))
    out = top.copy(); out[~m, 3] = 0; return out.astype(np.uint8)
meta = {}
for cid, stages in CHARS.items():
    if len(stages) == 4:
        A3, A, A1, B = map(load, stages)
        outs = [('A3', A3), ('A', A), ('A1', A1), ('B', B), ('c2', diff(A3, A)), ('c1', diff(A, A1)), ('c0', diff(A1, B))]
    else:
        A, A1, B = map(load, stages)
        outs = [('A', A), ('A1', A1), ('B', B), ('c1', diff(A, A1)), ('c0', diff(A1, B))]
    for n, arr in outs:
        Image.fromarray(arr.astype(np.uint8)).save(f'../web/art/{cid}_{n}.png')
    h, w = B.shape[:2]
    x0, y0, x1, y1 = Image.fromarray(B.astype(np.uint8)).getbbox()
    H = y1 - y0
    # torso centre from the bare stage: median x of opaque pixels in the chest band
    band = B[y0 + int(.18 * H): y0 + int(.45 * H), :, 3] > 0
    xs = np.nonzero(band)[1]; cx = float(np.median(xs)) if len(xs) else w / 2
    s = .95
    meta[cid] = {
        'w': w, 'h': h, 'layers3': len(stages) == 4,
        't': {'s': s, 'x': round(50 - cx * s, 1), 'y': round(-20 - y0 * s, 1)},
        'head': [round(cx), round(y0 + .08 * H), round(.09 * w), round(.08 * H)],
        'pec': [round(cx), round(y0 + .21 * H), round(.2 * w), round(.055 * H)],
        'belly': [round(cx), round(y0 + (.55 if cid in REAR else .43) * H), round(.18 * w), round(.08 * H)],
    }
json.dump(meta, open('../web/art/art.json', 'w'), indent=1)
print(json.dumps(meta))
