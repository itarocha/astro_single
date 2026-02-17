"""Runner mínimo: gera `mapa.png` usando `data.py` e `chart.py`.
Suporta modo estático (gera PNG) e modo interativo (Tkinter).

Instalação: pip install -r requirements.txt
Uso:
  python index.py            # gera mapa.png
  python index.py --interactive  # abre janela Tkinter
"""
import argparse
from chart import draw_map
import data


def main():
    p = argparse.ArgumentParser(description='Gerador de mapa astral (Pillow/Tkinter)')
    p.add_argument('--interactive', action='store_true', help='Abrir modo interativo (Tkinter)')
    p.add_argument('--size', type=int, default=800, help='Tamanho da imagem/janela (px)')
    args = p.parse_args()

    if args.interactive:
        try:
            from gui import run_gui
        except Exception as e:
            print('Não foi possível iniciar GUI:', e)
            return
        run_gui(data.BODIES, data.CUSPS, size=args.size)
    else:
        print('Gerando mapa estático: mapa.png')
        out = draw_map(data.BODIES, data.CUSPS, filename='mapa.png', size=args.size)
        print('Arquivo salvo em', out)


if __name__ == '__main__':
    main()
