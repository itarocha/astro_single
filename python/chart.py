from PIL import Image, ImageDraw, ImageFont
import math
from typing import List

def deg_to_rad(deg: float) -> float:
    return deg * math.pi / 180.0

def astro_angle(deg: float) -> float:
    return deg_to_rad(deg - 90.0)

def polar_to_xy(cx: int, cy: int, r: float, deg: float) -> tuple[float, float]:
    a = astro_angle(deg)
    x = cx + r * math.cos(a)
    y = cy + r * math.sin(a)
    return (x, y)

def angle_diff(a: float, b: float) -> float:
    d = abs((a - b + 360) % 360)
    return d if d <= 180 else 360 - d

ASPECTS = [
    {'name':'Conjunção','angle':0,'orbe':8,'color':'#444444'},
    {'name':'Sextil','angle':60,'orbe':6,'color':'#2E86AB'},
    {'name':'Quadratura','angle':90,'orbe':6,'color':'#C0392B'},
    {'name':'Trígono','angle':120,'orbe':6,'color':'#27AE60'},
    {'name':'Oposição','angle':180,'orbe':8,'color':'#8E44AD'}
]

def get_aspect(a: float, b: float):
    d = angle_diff(a, b)
    for asp in ASPECTS:
        if abs(d - asp['angle']) <= asp['orbe']:
            return asp
    return None

def draw_map(bodies: List[dict], cusps: List[float], filename: str = 'mapa.png', size: int = 800):
    W = H = size
    cx, cy = W // 2, H // 2
    R = min(cx, cy) - 20

    img = Image.new('RGBA', (W, H), 'white')
    draw = ImageDraw.Draw(img)

    # fundo: círculo externo
    draw.ellipse((cx-R, cy-R, cx+R, cy+R), outline='#222222', width=2)

    # signos (contornos simples)
    for i in range(12):
        start = i*30 - 90
        end = (i+1)*30 - 90
        draw.arc([cx-R, cy-R, cx+R, cy+R], start=start, end=end, fill='#cccccc', width=1)
        mid = i*30 + 15
        lx, ly = polar_to_xy(cx, cy, R-24, mid)
        draw.text((lx-10, ly-8), f'{i+1}', fill='black')

    # casas - linhas
    for i, deg in enumerate(cusps):
        x, y = polar_to_xy(cx, cy, R, deg)
        draw.line((cx, cy, x, y), fill='#888888', width=1)
        labx, laby = polar_to_xy(cx, cy, R-8, deg)
        draw.text((labx-6, laby-6), f'{i+1:02d}', fill='black')

    # planetas - marcadores
    for b in bodies:
        px, py = polar_to_xy(cx, cy, R-60, b['lon'])
        r = 6
        draw.ellipse((px-r, py-r, px+r, py+r), fill='black')
        draw.text((px+8, py-6), b.get('name', b.get('code', '')), fill='black')

    # aspectos
    for i in range(len(bodies)):
        for j in range(i+1, len(bodies)):
            a = bodies[i]['lon']
            b = bodies[j]['lon']
            asp = get_aspect(a, b)
            if not asp:
                continue
            p1 = polar_to_xy(cx, cy, R-60, a)
            p2 = polar_to_xy(cx, cy, R-60, b)
            draw.line((p1[0], p1[1], p2[0], p2[1]), fill=asp['color'], width=1)

    img.save(filename)
    return filename

if __name__ == '__main__':
    print('Este módulo fornece draw_map(bodies, cusps, filename, size)')
