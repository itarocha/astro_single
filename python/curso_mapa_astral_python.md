
# Curso Completo de Python + Desenho de Mapas Astrais
# Desenho de Mapa Astral Profissional — Versão Python

**Autor:** Itamar Rocha Chaves Junior (adaptação para Python)

Este documento é a versão do curso voltada para Python, com exemplos práticos usando bibliotecas comuns para desenho: `Pillow` (PIL) para imagens estáticas e `tkinter` para interface interativa. O foco é ensinar a construir um gerador de mapa astral profissional em Python, cobrindo matemática, modelagem de dados, desenho e recursos práticos.

Sumário
- Objetivos e pré-requisitos
- Estrutura do projeto em Python
- Fundamentos do desenho: Pillow vs Tkinter
- Matemática (graus/radianos e coordenadas)
- Zodíaco e setores
- Casas (cúspides)
- Planetas e pontos
- Aspectos astrológicos
- Organização em camadas e performance
- Exportação e integração
- Exercícios e próximos passos

Pré-requisitos
- Python 3.8+
- Instalar Pillow: `pip install pillow`
- Noções básicas de Python (funções, listas, dicionários)

Estrutura proposta do projeto (Python)
```
index.py          # script simples para gerar/visualizar o mapa
chart.py          # lógica principal de desenho
math_utils.py     # conversões e utilitários trigonométricos
zodiac.py         # desenho dos signos e legendas
houses.py         # manejo de cúspides
bodies.py         # modelagem e desenho dos corpos
aspects.py        # cálculo de aspectos
data.py           # dados de exemplo (posições, cúspides)
```

MÓDULO 1 — FUNDAMENTOS DO DESENHO EM PYTHON

1.1 Escolhendo a biblioteca

- Pillow: ótimo para gerar imagens estáticas (PNG/JPEG). API `Image`, `ImageDraw`.
- Tkinter: pronto para interfaces simples e interatividade (mouse, tooltips).
- Para gráficos vetoriais ou alta qualidade é possível usar `cairo`/`pycairo`.

Exemplo mínimo (Pillow):

```python
from PIL import Image, ImageDraw

W, H = 800, 800
img = Image.new('RGBA', (W, H), 'white')
draw = ImageDraw.Draw(img)
cx, cy = W // 2, H // 2
R = min(cx, cy) - 20
draw.ellipse((cx-R, cy-R, cx+R, cy+R), outline='#222', width=2)
img.save('mapa.png')
```

MÓDULO 2 — MATEMÁTICA DO MAPA ASTRAL

2.1 Graus e radianos

```python
import math

def deg_to_rad(deg: float) -> float:
    return deg * math.pi / 180.0

def rad_to_deg(rad: float) -> float:
    return rad * 180.0 / math.pi
```

2.2 Referencial astrológico

No canvas/browser usamos -90° de deslocamento para colocar 0° em Ascendente esquerdo. Mesma lógica vale em Python:

```python
def astro_angle(deg: float) -> float:
    return deg_to_rad(deg - 90.0)
```

2.3 Polar → cartesiano

```python
def polar_to_xy(cx: int, cy: int, r: float, deg: float) -> tuple[float, float]:
    a = astro_angle(deg)
    x = cx + r * math.cos(a)
    y = cy + r * math.sin(a)
    return (x, y)
```

Exemplo de uso com Pillow:

```python
px, py = polar_to_xy(cx, cy, R - 40, 120.5)
draw.rectangle((px-3, py-3, px+3, py+3), fill='black')
```

MÓDULO 3 — ZODÍACO

3.1 Conceitos

- 12 signos, 30° cada

```python
SIGNS = ['Áries','Touro','Gêmeos','Câncer','Leão','Virgem','Libra','Escorpião','Sagitário','Capricórnio','Aquário','Peixes']
```

3.2 Desenho dos setores com Pillow

O Pillow não tem um método direto para setores preenchidos com ângulos em graus; podemos desenhar arcos usando `ImageDraw.arc` e preencher usando máscaras ou polylines. Exemplo simples (contorno):

```python
for i, s in enumerate(SIGNS):
    start = i*30 - 90
    end = (i+1)*30 - 90
    # ImageDraw.arc usa ângulos em graus no sistema Pillow (0=3h, crescente anti-horário)
    draw.arc([cx-R, cy-R, cx+R, cy+R], start=start, end=end, fill='#ccc', width=1)
    mid = i*30 + 15
    lx, ly = polar_to_xy(cx, cy, R-24, mid)
    draw.text((lx, ly-7), s, fill='black')
```

Nota: para preenchimentos com transparência, construa uma máscara `Image.new('L', ...)` e desenhe setores nela.

MÓDULO 4 — CASAS (CÚSPIDES)

4.1 Cúspides (dados)

Forneça um array de 12 ângulos (graus). Exemplo:

```python
CUSPS = [82.70154304778679, 111.1341504020764, 141.3461512349346, 173.6225546549408, 205.73919610408942, 235.36167285257102, 262.7015430477868, 291.1341504020764, 321.3461512349346, 353.62255465494087, 25.73919610408942, 55.361672852571004]
```

4.2 Desenho das linhas das casas

```python
for i, deg in enumerate(CUSPS):
    x, y = polar_to_xy(cx, cy, R, deg)
    draw.line((cx, cy, x, y), fill='#888', width=1)
    lx, ly = polar_to_xy(cx, cy, R-8, deg)
    draw.text((lx-6, ly-6), f'{i+1:02d}', fill='black')
```

Exercício: preencha setores entre cúspides com gradação de cor usando uma máscara.

MÓDULO 5 — PLANETAS E PONTOS

5.1 Modelagem

Exemplo de estrutura de corpo:

```python
BODIES = [
    {'code':'sol', 'name':'Sol', 'lon':97.6625810835},
    {'code':'lua', 'name':'Lua', 'lon':307.4589777145},
    # ...
]
```

5.2 Desenho dos corpos

```python
for b in BODIES:
    px, py = polar_to_xy(cx, cy, R-60, b['lon'])
    r = 6
    draw.ellipse((px-r, py-r, px+r, py+r), fill='black')
    draw.text((px+8, py-6), b['name'], fill='black')
```

Dica: para evitar sobreposição de rótulos, calcule distâncias entre pontos e ajuste `y` ou `x` conforme necessário.

MÓDULO 6 — ASPECTOS ASTROLÓGICOS

6.1 Diferença angular

```python
def angle_diff(a: float, b: float) -> float:
    d = abs((a - b + 360) % 360)
    return d if d <= 180 else 360 - d
```

6.2 Definição de aspectos

```python
ASPECTS = [
    {'name':'Conjunção','angle':0,'orbe':8,'color':'#444'},
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
```

6.3 Desenho das linhas de aspecto

```python
for i in range(len(BODIES)):
    for j in range(i+1, len(BODIES)):
        a = BODIES[i]['lon']
        b = BODIES[j]['lon']
        asp = get_aspect(a, b)
        if not asp:
            continue
        p1 = polar_to_xy(cx, cy, R-60, a)
        p2 = polar_to_xy(cx, cy, R-60, b)
        draw.line((p1[0], p1[1], p2[0], p2[1]), fill=asp['color'], width=1)
```

Exercício: desenhe o nome do aspecto no centro da linha e calcule distância mínima para evitar sobreposição com outros rótulos.

MÓDULO 7 — INTERATIVIDADE (Tkinter)

Se quiser interação (hover, tooltips), `tkinter.Canvas` é uma opção leve:

```python
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=800, bg='white')
canvas.pack()
# desenhe usando canvas.create_oval, create_line, create_text
root.mainloop()
```

Para tooltips, associe eventos `<Motion>` e detecte proximidade de um ponto.

Boas práticas e performance

- Desenhe camadas estáticas em imagens separadas (Pillow) e reutilize-as.
- Use `Image.alpha_composite` para compor camadas com transparência.
- Em GUIs, só redesenhe a parte dinâmica ao invés de tudo.

Exportação

- Salvando PNG: `img.save('mapa.png')`
- Gerando PDF: converta a imagem para PDF com Pillow (`img.save('mapa.pdf', 'PDF')`) ou use `reportlab` para composições mais complexas.

Exercícios práticos

1. Implemente um script `index.py` que carrega `data.py` e gera `mapa.png` com Pillow.
2. Adicione um modo `--interactive` que abre uma janela Tkinter com destaque ao passar o mouse.
3. Parseie o bloco de dados do arquivo original (lon e cusps) e carregue em `data.py` automaticamente.

Dados de exemplo

Inclua no `data.py` arrays `BODIES` e `CUSPS` com os valores do arquivo original para testar.

Próximos passos

- Integrar Swiss Ephemeris via wrappers para Python
- Implementar diferentes sistemas de casas
- Adicionar exportação vetorial (SVG) usando `svgwrite` ou `cairosvg`

---

Se quiser, posso agora:
- Gerar a implementação mínima em Python (`index.py`, `chart.py`, `data.py`) com Pillow e exemplo de `Tkinter`.
- Criar a versão `data.py` parseando automaticamente o bloco de exemplo existente no repositório.

Diga qual opção prefere que eu implemente primeiro.