import tkinter as tk
from typing import List
from chart import polar_to_xy, get_aspect
import math


def run_gui(bodies: List[dict], cusps: List[float], size: int = 800):
    W = H = size
    cx, cy = W // 2, H // 2
    R = min(cx, cy) - 20

    root = tk.Tk()
    root.title('Mapa Astral - Interativo')
    canvas = tk.Canvas(root, width=W, height=H, bg='white')
    canvas.pack()

    # desenhar círculo externo
    canvas.create_oval(cx-R, cy-R, cx+R, cy+R, outline='#222222', width=2)

    # desenhar casas (linhas)
    for i, deg in enumerate(cusps):
        x, y = polar_to_xy(cx, cy, R, deg)
        canvas.create_line(cx, cy, x, y, fill='#888888')
        lx, ly = polar_to_xy(cx, cy, R-8, deg)
        canvas.create_text(lx, ly, text=f'{i+1:02d}', fill='black')

    # desenhar planetas e armazenar posições
    planet_items = []  # tuples (id, bbox, data)
    for b in bodies:
        px, py = polar_to_xy(cx, cy, R-60, b['lon'])
        r = 6
        oid = canvas.create_oval(px-r, py-r, px+r, py+r, fill='black')
        tid = canvas.create_text(px+8, py, text=b.get('name', b.get('code', '')), anchor='w')
        planet_items.append({'oid': oid, 'x': px, 'y': py, 'data': b})

    # desenhar aspectos
    for i in range(len(bodies)):
        for j in range(i+1, len(bodies)):
            a = bodies[i]['lon']
            b = bodies[j]['lon']
            asp = get_aspect(a, b)
            if not asp:
                continue
            p1 = polar_to_xy(cx, cy, R-60, a)
            p2 = polar_to_xy(cx, cy, R-60, b)
            canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill=asp['color'])

    # tooltip
    tooltip = canvas.create_text(10, 10, text='', anchor='nw', fill='black', state='hidden', font=('Arial', 10, 'normal'))

    def on_move(event):
        x, y = event.x, event.y
        found = None
        for p in planet_items:
            dx = x - p['x']
            dy = y - p['y']
            if dx*dx + dy*dy <= 8*8:
                found = p
                break
        if found:
            info = f"{found['data'].get('name')}\nlon: {found['data'].get('lon'):.3f}°"
            canvas.itemconfigure(tooltip, text=info)
            canvas.coords(tooltip, x+12, y+12)
            canvas.itemconfigure(tooltip, state='normal')
        else:
            canvas.itemconfigure(tooltip, state='hidden')

    canvas.bind('<Motion>', on_move)

    root.mainloop()


if __name__ == '__main__':
    print('Este módulo fornece run_gui(bodies, cusps, size) para modo interativo.')
