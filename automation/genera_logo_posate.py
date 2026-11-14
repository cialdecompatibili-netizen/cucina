# Logo + favicon "forchetta e coltello" (bianchi su quadrato arrotondato coi colori di _data/tema.json). Forme grosse e senza testo: si legge anche a 16px.
# Uso, dalla radice del sito:  python automation/genera_logo_posate.py
# Scrive gli stessi file di genera_logo.py: assets/images/favicon.svg, favicon-32/192/512.png, logo-72.png, apple-touch-icon.png, favicon.ico (anche nella radice).
import json, os
from PIL import Image, ImageDraw
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, 'assets', 'images')
def hx(s): s = s.lstrip('#'); return tuple(int(s[i:i+2], 16) for i in (0, 2, 4))
def mix(a, b, t): return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))
def h(c): return '#%02x%02x%02x' % c
tema = json.load(open(os.path.join(ROOT, '_data', 'tema.json'), encoding='utf-8'))
TOP = mix(hx(tema['accent']), (255, 255, 255), .10); BOT = hx(tema['accent_dark'])
# rettangoli (x, y, larghezza, altezza, raggio) su griglia 64x64
RECTS = [(11.3, 9, 4.4, 19, 2.2), (18.8, 9, 4.4, 19, 2.2), (26.3, 9, 4.4, 19, 2.2),  # rebbi
         (11.3, 24, 19.4, 7.5, 3.7),                                                   # base forchetta
         (18.8, 28, 4.4, 27, 2.2),                                                     # manico forchetta
         (42, 36, 7, 19, 3.2)]                                                         # manico coltello
BLADE = 'M40 9 Q51 11 51 25 L51 38 L40 38 Z'
def blade_pts(n=24):
    p0, p1, p2 = (40, 9), (51, 11), (51, 25); pts = []
    for i in range(n + 1):
        t = i / n; pts.append(((1-t)**2*p0[0] + 2*(1-t)*t*p1[0] + t*t*p2[0], (1-t)**2*p0[1] + 2*(1-t)*t*p1[1] + t*t*p2[1]))
    return pts + [(51, 38), (40, 38)]
svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="s" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient></defs>'
       '<rect width="64" height="64" rx="14" fill="url(#s)"/><g fill="#fff">%s<path d="%s"/></g></svg>\n'
       % (h(TOP), h(BOT), ''.join('<rect x="%s" y="%s" width="%s" height="%s" rx="%s"/>' % r for r in RECTS), BLADE))
open(os.path.join(IMG, 'favicon.svg'), 'w', encoding='utf-8', newline='\n').write(svg)
def render(N, tondo=True):
    S = 8; M = N * S; k = M / 64
    g = Image.new('RGB', (1, M))
    for y in range(M): g.putpixel((0, y), mix(TOP, BOT, y / (M - 1)))
    im = Image.new('RGBA', (M, M), (0, 0, 0, 0))
    mask = Image.new('L', (M, M), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, M - 1, M - 1), radius=int(14 * k) if tondo else 0, fill=255)
    im.paste(g.resize((M, M)).convert('RGBA'), (0, 0), mask)
    d = ImageDraw.Draw(im)
    for x, y, w, hh, r in RECTS: d.rounded_rectangle((x*k, y*k, (x+w)*k, (y+hh)*k), radius=r*k, fill=(255, 255, 255, 255))
    d.polygon([(a*k, b*k) for a, b in blade_pts()], fill=(255, 255, 255, 255))
    return im.resize((N, N), Image.LANCZOS)
for n, name in ((32, 'favicon-32.png'), (72, 'logo-72.png'), (192, 'favicon-192.png'), (512, 'favicon-512.png')):
    render(n).save(os.path.join(IMG, name))
render(180, tondo=False).convert('RGB').save(os.path.join(IMG, 'apple-touch-icon.png'))
ico = render(256)
for p in (os.path.join(IMG, 'favicon.ico'), os.path.join(ROOT, 'favicon.ico')): ico.save(p, sizes=[(16, 16), (32, 32), (48, 48)])
# anteprima piccola per controllo leggibilita' (non pubblicata)
render(16).resize((160, 160), Image.NEAREST).save(os.path.join(os.environ.get('TEMP', '.'), 'anteprima_16.png'))
print('logo posate scritto', h(TOP), h(BOT))
