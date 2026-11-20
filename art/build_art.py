"""Turn generated stages into game layers: web/art/<id>_{A,A1,B,c1,c0}.png + web/art/art.json (bounce regions, card placement)."""
import json
import numpy as np
from PIL import Image
# id: (full outfit, outer layer gone, bare). Characters with one clothing layer reuse A for A1.
CHARS = {
  'ben':    ('pilot/ben2_flash_0.png', 'pilot/ben2_A1_0.png', 'pilot/ben2_B_0.png'),
  'jompon': ('chars/jompon_A_0.png', 'chars/jompon_A1b_0.png', 'chars/jompon_B_0.png'),
  'dave':   ('chars/dave_A_0.png', 'chars/dave_A1_0.png', 'chars/dave_B2_0.png'),
  'champ':  ('chars/champ_A_0.png', 'chars/champ_A1n_0.png', 'chars/champ_B_0.png'),
  'ton':    ('chars/ton_A_0.png', 'chars/ton_A_0.png', 'chars/ton_B_0.png'),
  'ming':   ('chars/ming_A_0.png', 'chars/ming_A_0.png', 'chars/ming_B_0.png'),
  'jay':    ('chars/jay_A2_0.png', 'chars/jay_A2_0.png', 'chars/jay_B_0.png'),
  'dan':    ('chars/dan_A_0.png', 'chars/dan_A1_0.png', 'chars/dan_B5_0.png'),
  'fah':    ('chars/fah_A_0.png', 'chars/fah_A_0.png', 'chars/fah_Bp_0.png'),
  'q':      ('chars/q_A_0.png', 'chars/q_A_0.png', 'chars/q_B_0.png'),
  'tiger':  ('chars/tiger_A_0.png', 'chars/tiger_A1n_0.png', 'chars/tiger_B_0.png'),
  'non':    ('chars/non_A_0.png', 'chars/non_A1n_0.png', 'chars/non_B_0.png'),
  'wchain': ('chars/wchain_A_0.png', 'chars/wchain_A1_0.png', 'chars/wchain_B_0.png'),
  'wneedle': ('chars/wneedle_A_0.png', 'chars/wneedle_A1_0.png', 'chars/wneedle_B_0.png'),
  'wchub': ('chars/wchub_A_0.png', 'chars/wchub_A1f_0.png', 'chars/wchub_Bf_0.png'),
  'wsumo': ('chars/wsumo_A_0.png', 'chars/wsumo_A1_0.png', 'chars/wsumo_B_0.png'),
  'wbutler': ('chars/wbutler_A_0.png', 'chars/wbutler_A1f_0.png', 'chars/wbutler_Bf_0.png'),
  'wgorilla': ('chars/wgorilla_A_0.png', 'chars/wgorilla_A1f_0.png', 'chars/wgorilla_Bf_0.png'),
  # 3-layer boss: (A3 full, A two layers, A1 one layer, B bare)
  'tong': ('chars/tong_A_0.png', 'chars/tong_A1f_0.png', 'chars/tong_B_0.png'),
  'bork': ('chars/bork_A_0.png', 'chars/bork_A1f_0.png', 'chars/bork_B_0.png'),
  'daigo': ('chars/daigo_A_0.png', 'chars/daigo_A1_0.png', 'chars/daigo_Bf_0.png'),
  'boon': ('chars/boon_A_0.png', 'chars/boon_A1_0.png', 'chars/boon_Bf_0.png'),
  'keng': ('chars/keng_A_0.png', 'chars/keng_A1f_0.png', 'chars/keng_B_0.png'),
  'phum': ('chars/phum_A_0.png', 'chars/phum_A1f_0.png', 'chars/phum_Bf_0.png'),
  'marin': ('chars/marin_A_0.png', 'chars/marin_A1f_0.png', 'chars/marin_B_0.png'),
  'ek': ('chars/ek_A_0.png', 'chars/ek_A1_0.png', 'chars/ek_Bf_0.png'),
  'singh': ('chars/singh_Af_0.png', 'chars/singh_A1f_0.png', 'chars/singh_Bf_0.png'),
  'phupha': ('chars/phupha_Af_0.png', 'chars/phupha_A1f_0.png', 'chars/phupha_Bf_0.png'),
  'takeshi': ('chars/takeshi_A_0.png', 'chars/takeshi_A1_0.png', 'chars/takeshi_Bc_0.png'),
  'talay': ('chars/talay_A_0.png', 'chars/talay_A1_0.png', 'chars/talay_B_0.png'),
  'plerng': ('chars/plerng_A_0.png', 'chars/plerng_A1_0.png', 'chars/plerng_Bf_0.png'),
  'sak': ('chars/sak_A_0.png', 'chars/sak_A1_0.png', 'chars/sak_B_0.png'),
  'oat': ('chars/oat_A_0.png', 'chars/oat_A1_0.png', 'chars/oat_B_0.png'),
  'somsak': ('chars/somsak_A_0.png', 'chars/somsak_A1_0.png', 'chars/somsak_B_0.png'),
  'tex': ('chars/tex_A_0.png', 'chars/tex_A1_0.png', 'chars/tex_B_0.png'),
  'boat': ('chars/boat_A_0.png', 'chars/boat_A1_0.png', 'chars/boat_Bf_0.png'),
  'gunman': ('chars/gunman_A_0.png', 'chars/gunman_A2_0.png', 'chars/gunman_A1_0.png', 'chars/gunman_B_0.png'),
  'kan': ('chars/kan_A_0.png', 'chars/kan_A1_0.png', 'chars/kan_B_0.png'),
  'max': ('chars/max_A_0.png', 'chars/max_A1_0.png', 'chars/max_B_0.png'),
  'dealer': ('chars/dealer_A_0.png', 'chars/dealer_A2_0.png', 'chars/dealer_A1_0.png', 'chars/dealer_B_0.png'),
  'ace': ('chars/ace_A_0.png', 'chars/ace_A1_0.png', 'chars/ace_Bj_0.png'),
  'general': ('chars/general_A_0.png', 'chars/general_A2f_0.png', 'chars/general_A1_0.png', 'chars/general_B_0.png'),
  'arthur': ('chars/arthur_A_0.png', 'chars/arthur_A1_0.png', 'chars/arthur_B_0.png'),
  'chueak': ('chars/chueak_A_0.png', 'chars/chueak_A1_0.png', 'chars/chueak_Bf_0.png'),
  'dracula': ('chars/dracula_A_0.png', 'chars/dracula_A1f_0.png', 'chars/dracula_B_0.png'),
  'boxer': ('chars/boxer_A_0.png', 'chars/boxer_A2_0.png', 'chars/boxer_A1_0.png', 'chars/boxer_B_0.png'),
  'hunter': ('chars/hunter_A_0.png', 'chars/hunter_A2_0.png', 'chars/hunter_A1c_0.png', 'chars/hunter_Bc_0.png'),
}
REAR = {'ming', 'jay', 'talay', 'ace', 'chueak'}   # back-turned poses: the soft-body region is the butt, not the belly
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
# hand-placed soft-body regions (sprite px) override the automatic guesses
REG = json.load(open('regions.json'))
for cid, r in REG.items():
    if cid in meta:
        for k in ('head', 'pec', 'belly'): meta[cid][k] = r.get(k, meta[cid][k])
        for k in ('crotch', 'butt'):
            if k in r: meta[cid][k] = r[k]
json.dump(meta, open('../web/art/art.json', 'w'), indent=1)
print(json.dumps(meta))
