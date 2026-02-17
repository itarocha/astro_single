# Curso Mapa Astral (Python)

Gerador de mapa astral simples em Python usando `Pillow` para saída estática e `tkinter` para modo interativo.

Requisitos

- Python 3.8+
- Instalar dependências:

```bash
pip install -r requirements.txt
```

Como usar

- Gerar imagem estática `mapa.png`:

```bash
python index.py
```

- Abrir modo interativo (janela com tooltip):

```bash
python index.py --interactive
```

Arquivos principais

- `index.py` — runner; gera imagem ou abre GUI
- `chart.py` — funções de desenho (Pillow)
- `gui.py` — modo interativo com `tkinter`
- `data.py` — dados de exemplo (posições e cúspides)

Notas

- `tkinter` faz parte da biblioteca padrão do Python na maioria das distribuições. Em algumas instalações (Linux) pode ser necessário instalar o pacote do sistema (ex: `sudo apt install python3-tk`).
- Este projeto é uma implementação mínima para fins didáticos. Para cálculos astrológicos precisos, integre uma ephemeris (Swiss Ephemeris).

Próximos passos

- Integrar parsing automático dos blocos de dados do esboço
- Implementar detecção e resolução de colisão de rótulos
- Adicionar exportação vetorial (SVG, PDF)
