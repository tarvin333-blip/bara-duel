"""Turn generated stages into game layers: web/art/<id>_{A,A1,B,c1,c0}.png + web/art/art.json (bounce regions, card placement)."""
import json
import numpy as np
from PIL import Image
# id: (full outfit, outer layer gone, bare). Characters with one clothing layer reuse A for A1.
CHARS = {
  'vito': ('chars/vito_A_0.png', 'chars/vito_A1_0.png', 'chars/vito_B2_0.png'),
  'bruin': ('chars/bruin_A_0.png', 'chars/bruin_A1_0.png', 'chars/bruin_B2_0.png'),
  'wade': ('chars/wade_A_0.png', 'chars/wade_A1_0.png', 'chars/wade_B2_0.png'),
  'gunnar': ('chars/gunnar_A_0.png', 'chars/gunnar_A1_0.png', 'chars/gunnar_B2_0.png'),
  'ellis': ('chars/ellis_A_0.png', 'chars/ellis_A1_0.png', 'chars/ellis_B2_0.png'),
  'tane': ('chars/tane_A_0.png', 'chars/tane_A1_0.png', 'chars/tane_B2_0.png'),
  'blaze': ('chars/blaze_A_0.png', 'chars/blaze_A1_0.png', 'chars/blaze_B2_0.png'),
  'graham': ('chars/graham_A_0.png', 'chars/graham_A1_0.png', 'chars/graham_B2_0.png'),
  'rhys': ('chars/rhys_A_0.png', 'chars/rhys_A1_0.png', 'chars/rhys_B2_0.png'),
  'gus': ('chars/gus_A_0.png', 'chars/gus_A1_0.png', 'chars/gus_B2_0.png'),
  'krit': ('chars/krit_A_0.png', 'chars/krit_A1_0.png', 'chars/krit_B2_0.png'),
  'nate': ('chars/nate_A_0.png', 'chars/nate_A1_0.png', 'chars/nate_B2_0.png'),
  'rusty':  ('chars/rusty_AF_0.png', 'chars/rusty_A1F_0.png', 'chars/rusty_B2F_0.png'),
  'enzo':   ('chars/enzo2_A_0.png', 'chars/enzo2_A1_0.png', 'chars/enzo2_B2_0.png'),
  'aldric': ('chars/aldric_A_0.png', 'chars/aldric_A1_0.png', 'chars/aldric_B2_0.png'),
  'leo':    ('chars/leo_A_0.png', 'chars/leo_A1_0.png', 'chars/leo_B2_0.png'),
  'kenji':  ('chars/kenji_A_0.png', 'chars/kenji_A1_0.png', 'chars/kenji_B2_0.png'),
  'hugo':   ('chars/hugo_A_0.png', 'chars/hugo_A1_0.png', 'chars/hugo_B2_0.png'),
  'papa':   ('chars/papa2_A_0.png', 'chars/papa2_A1_0.png', 'chars/papa2_B2_0.png'),
  'ivan':   ('chars/ivan_AF_0.png', 'chars/ivan_A1F_0.png', 'chars/ivan_B2F_0.png'),
  'morse':  ('chars/morse_AF_0.png', 'chars/morse_A1F_0.png', 'chars/morse_B2F_0.png'),
  'marco':  ('chars/marco_A_0.png', 'chars/marco_A1_0.png', 'chars/marco_B2_0.png'),
  'lucien': ('chars/lucien_A_0.png', 'chars/lucien_A1_0.png', 'chars/lucien_B2_0.png'),
  'zahir':  ('chars/zahir_A_0.png', 'chars/zahir_A1_0.png', 'chars/zahir_B2_0.png'),
  'finn':   ('chars/finn_A_0.png', 'chars/finn_A1_0.png', 'chars/finn_B2_0.png'),
  'bruto':  ('chars/bruto_A_0.png', 'chars/bruto_A1_0.png', 'chars/bruto_B2_0.png'),
  'cliff':  ('chars/cliff_A_0.png', 'chars/cliff_A1_0.png', 'chars/cliff_B2_0.png'),
  'ulf':    ('chars/ulf_A_0.png', 'chars/ulf_A1_0.png', 'chars/ulf_B2_0.png'),
  'hank':   ('chars/hank_A_0.png', 'chars/hank_A1_0.png', 'chars/hank_B2_0.png'),
  'otto':   ('chars/otto_A_0.png', 'chars/otto_A1_0.png', 'chars/otto_B2_0.png'),
  'brick':  ('chars/brick_A_0.png', 'chars/brick_A1_0.png', 'chars/brick_B2_0.png'),
  'frost':  ('chars/frost_AF_0.png', 'chars/frost_A1_0.png', 'chars/frost_B2F_0.png'),
  'ren':    ('chars/ren_A_0.png', 'chars/ren_A1_0.png', 'chars/ren_B2_0.png'),
  'taurus': ('chars/taurus_A_0.png', 'chars/taurus_A1_0.png', 'chars/taurus_B2_0.png'),
  'vance':  ('chars/vance_A_0.png', 'chars/vance_A1_0.png', 'chars/vance_B2_0.png'),
  'koa':    ('chars/koa_A_0.png', 'chars/koa_A1_0.png', 'chars/koa_B2_0.png'),
  'zack':   ('chars/zack_A_0.png', 'chars/zack_A1_0.png', 'chars/zack_B2_0.png'),
  'duke':   ('chars/duke_AF_0.png', 'chars/duke_A1F_0.png', 'chars/duke_B2F_0.png'),
  'taiko':  ('chars/taiko_AF_0.png', 'chars/taiko_A1F_0.png', 'chars/taiko_B3F_0.png'),
  'cosmo':  ('chars/cosmo_A_0.png', 'chars/cosmo_A1_0.png', 'chars/cosmo_B3_0.png'),
  'hawk':   ('chars/hawk_A_0.png', 'chars/hawk_A1_0.png', 'chars/hawk_B2_0.png'),
  'buck':   ('chars/buck_A_0.png', 'chars/buck_A1_0.png', 'chars/buck_B2_0.png'),
  'bruno':  ('chars/bruno_A_0.png', 'chars/bruno_A1_0.png', 'chars/bruno_B2_0.png'),
  'barbo':  ('chars/barbo_A_0.png', 'chars/barbo_A1_0.png', 'chars/barbo_B2_0.png'),
  'toro':   ('chars/toro_A_0.png', 'chars/toro_A1_0.png', 'chars/toro_B3_0.png'),
  'wanorn': ('chars/wanorn_AF_0.png', 'chars/wanorn_A1F_0.png', 'chars/wanorn_BF_0.png'),
  'rocco':  ('chars/rocco_A_0.png', 'chars/rocco_A1_0.png', 'chars/rocco_B2_0.png'),
  'axel':   ('chars/axel_AF_0.png', 'chars/axel_A1F_0.png', 'chars/axel_B3F_0.png'),
  'jim':    ('chars/jim_A_0.png', 'chars/jim_A1_0.png', 'chars/jim_B2_0.png'),
  'kai':    ('chars/kai_AF_0.png', 'chars/kai_A1F_0.png', 'chars/kai_BF_0.png'),
  'gilga':  ('chars/gilga_A_0.png', 'chars/gilga_A1_0.png', 'chars/gilga_B_0.png'),
  'rex':    ('chars/rex_A_0.png', 'chars/rex_A1_0.png', 'chars/rex_B_0.png'),
  'chai':   ('chars/chai_A_0.png', 'chars/chai_A1_0.png', 'chars/chai_B_0.png'),
  'beowulf': ('chars/beow2_A_0.png', 'chars/beow2_A1_0.png', 'chars/beow2_B2_0.png'),
  'ben':    ('pilot/ben2_flash_0.png', 'pilot/ben2_A1_0.png', 'pilot/ben2_B_0.png'),
  'jompon': ('chars/jompon_A_0.png', 'chars/jompon_A1b_0.png', 'chars/jompon_B_0.png'),
  'dave':   ('chars/dave_A_0.png', 'chars/dave_A1_0.png', 'chars/dave_B2_0.png'),
  'champ':  ('chars/champ_A_0.png', 'chars/champ_A1n_0.png', 'chars/champ_Bm_0.png'),
  'ton':    ('chars/ton_A_0.png', 'chars/ton_A1m_0.png', 'chars/ton_B_0.png'),
  'ming':   ('chars/ming_A_0.png', 'chars/ming_A1m_0.png', 'chars/ming_B_0.png'),
  'jay':    ('chars/jay_A2_0.png', 'chars/jay_A1m_0.png', 'chars/jay_B_0.png'),
  'dan':    ('chars/dan_A_0.png', 'chars/dan_A1_0.png', 'chars/dan_B5_0.png'),
  'fah':    ('chars/fah_A_0.png', 'chars/fah_A_0.png', 'chars/fah_Bp_0.png'),
  'q':      ('chars/q_A_0.png', 'chars/q_A1m_0.png', 'chars/q_B_0.png'),
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
  'magician': ('chars/magician_A_0.png', 'chars/magician_A2_0.png', 'chars/magician_A1_0.png', 'chars/magician_B_0.png'),
  'kong': ('chars/kong_A_0.png', 'chars/kong_A1_0.png', 'chars/kong_B_0.png'),
  'vael': ('chars/vael_A_0.png', 'chars/vael_A2_0.png', 'chars/vael_A1f_0.png', 'chars/vael_Bf_0.png'),
  'hercules': ('chars/hercules_A_0.png', 'chars/hercules_A1_0.png', 'chars/hercules_B_0.png'),
  'robin': ('chars/robin_A_0.png', 'chars/robin_A1_0.png', 'chars/robin_B_0.png'),
  'lancelot': ('chars/lancelot_A_0.png', 'chars/lancelot_A1_0.png', 'chars/lancelot_B_0.png'),
  'boxer': ('chars/boxer_A_0.png', 'chars/boxer_A2_0.png', 'chars/boxer_A1_0.png', 'chars/boxer_B_0.png'),
  'hunter': ('chars/hunter_A_0.png', 'chars/hunter_A2_0.png', 'chars/hunter_A1c_0.png', 'chars/hunter_Bc_0.png'),
}
REAR = {'tane', 'rhys', 'aldric', 'hugo', 'brick', 'koa', 'ming', 'jay', 'talay', 'ace', 'chueak', 'robin', 'lancelot'}   # back-turned poses: the soft-body region is the butt, not the belly
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
