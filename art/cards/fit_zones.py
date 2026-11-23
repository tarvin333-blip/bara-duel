"""Fit a wide pose onto the card: the largest scale (<= MAXK) where every opaque pixel stays inside the layout zones
(top overflow y>=40; x 16-1008 above y 960; x 112-912 below), feet on y=1290.
usage: python3 fit_zones.py SRC OUT [MAXK]"""
import sys
from PIL import Image
import numpy as np
src, out = sys.argv[1], sys.argv[2]; maxk = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
im = Image.open(src).convert('RGBA'); m = np.asarray(im)[:, :, 3] > 40
ys, xs = np.where(m); feet = ys.max(); sel = np.random.default_rng(0).choice(len(xs), min(len(xs), 40000), replace=False); ys, xs = ys[sel], xs[sel]
for k in np.arange(maxk, .4, -.005):
    Y = 1290 - (feet - ys) * k
    if (Y < 40).any(): continue
    for cx in range(300, 724, 4):
        X = cx + (xs - im.width / 2) * k; hi = Y < 960
        if (X[hi] >= 16).all() and (X[hi] <= 1008).all() and (X[~hi] >= 112).all() and (X[~hi] <= 912).all():
            sc = im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)
            o = Image.new('RGBA', (1024, 1536), (0, 0, 0, 0)); o.paste(sc, (round(cx - im.width / 2 * k), round(1290 - feet * k)), sc)
            o.save(out, quality=90, method=6); print(f'k={k:.3f} cx={cx}'); sys.exit()
print('no fit')
