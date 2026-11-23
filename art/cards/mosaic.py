"""Stepped-ellipse grid mosaic patch for a fitted card image.
usage: python3 mosaic.py IMG OUT CX CY RX RY [CELL] [DARK_BAND_X0 DARK_BAND_X1]
Prints the patch's top-left (x, y) on the 1024x1536 canvas.
With a dark band (e.g. a weapon handle in front), cells that are mostly that dark object keep its colour, other cells average skin only."""
import sys
from PIL import Image
import numpy as np
f, out, cx, cy, rx, ry = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:7])
B = int(sys.argv[7]) if len(sys.argv) > 7 else 20
band = tuple(map(int, sys.argv[8:10])) if len(sys.argv) > 9 else None
im = np.asarray(Image.open(f).convert('RGBA')).astype(float)
nx, ny = (2 * rx) // B + 2, (2 * ry) // B + 2
gx0 = (band[0] - B * ((band[0] - (cx - rx)) // B + 1)) if band else cx - nx * B // 2
gy0 = cy - ny * B // 2
reg = im[gy0:gy0 + ny * B, gx0:gx0 + nx * B]
lum = .3 * reg[:, :, 0] + .59 * reg[:, :, 1] + .11 * reg[:, :, 2]
cols = np.arange(nx * B) + gx0
dark = (lum < 125) & (((cols >= band[0]) & (cols <= band[1]))[None, :] if band else False) & (reg[:, :, 3] > 20)
o = np.zeros_like(reg)
for j in range(ny):
    for i in range(nx):
        x, y = gx0 + i * B + B / 2, gy0 + j * B + B / 2
        if ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 > 1: continue
        blk = reg[j*B:(j+1)*B, i*B:(i+1)*B]; al = blk[:, :, 3] > 20; hb = dark[j*B:(j+1)*B, i*B:(i+1)*B]
        if al.mean() < .5: continue
        use = hb if hb.mean() > .45 else (al & ~hb)
        if use.sum() < 5: use = al
        o[j*B:(j+1)*B, i*B:(i+1)*B, :3] = blk[use][:, :3].mean(0); o[j*B:(j+1)*B, i*B:(i+1)*B, 3] = 255
Image.fromarray(o.astype(np.uint8), 'RGBA').save(out); print(gx0, gy0)
