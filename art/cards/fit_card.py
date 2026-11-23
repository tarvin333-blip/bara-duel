"""Fit a character image onto the over-frame card layout (docs/card/card_template_guide.png).
usage: python3 fit_card.py SRC OUT HEIGHT_CM HEAD_X0 HEAD_X1 [BODY_X0 BODY_X1]
  head band: x range that contains the head (top of head = topmost opaque pixel there)
  body band: x range used to find the lowest boot pixel (leave out staffs or props that reach lower)
Feet land on y=1290, head-to-feet height = 1120 * HEIGHT_CM / 193 (Brannok is the reference), body centred on x=512."""
import sys
from PIL import Image
import numpy as np
src, out, hcm, hx0, hx1 = sys.argv[1], sys.argv[2], float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
bx0, bx1 = (int(sys.argv[6]), int(sys.argv[7])) if len(sys.argv) > 7 else (0, 10**6)
im = Image.open(src).convert('RGBA'); m = np.asarray(im)[:, :, 3] > 40
head = np.where(m[:, hx0:hx1].any(1))[0].min()
body = m[:, bx0:bx1]; feet = np.where(body.any(1))[0].max()
xs = np.where(m.any(0))[0]; cx = (xs.min() + xs.max()) / 2
k = 1120 * hcm / 193 / (feet - head)
sc = im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)
o = Image.new('RGBA', (1024, 1536), (0, 0, 0, 0)); o.paste(sc, (round(512 - cx * k), round(1290 - feet * k)), sc)
a = np.asarray(o)[:, :, 3] > 40; ys, xs2 = np.where(a)
print(f'k={k:.3f} head={head} feet={feet} -> bbox x {xs2.min()}-{xs2.max()} y {ys.min()}-{ys.max()}')
o.save(out, quality=90, method=6)
