
# Curso Completo
## JavaScript + Canvas HTML5 para Desenho de Mapa Astral

Autor: Curso técnico baseado em dados reais de mapa astral  
Formato: Apostila didática em Markdown

---

## Apresentação

Esta apostila acompanha o curso **JavaScript e Canvas HTML5 para Desenho de Mapa Astral**.
O objetivo é ensinar, passo a passo, como construir programaticamente um **mapa astral completo**
sem depender de bibliotecas gráficas externas, entendendo profundamente:

- Matemática angular
- Sistema de coordenadas do Canvas
- Estrutura de um mapa astrológico
- Organização profissional de código

Todos os exemplos utilizam dados reais do mapa natal de:

**Itamar Rocha Chaves Junior**  
Caxias – MA  
29/06/1972 – 05:00 (UTC-3)

---

## Módulo 1 – Introdução ao Canvas HTML5

### 1.1 O que é o Canvas

O elemento `<canvas>` do HTML5 fornece uma área de desenho controlada inteiramente por JavaScript.
Diferente de HTML tradicional, o Canvas não possui elementos internos: tudo precisa ser desenhado.

Características:
- Renderização imediata
- Controle total de pixels
- Ideal para gráficos, jogos e visualizações científicas

### 1.2 Sistema de Coordenadas

O Canvas utiliza um sistema cartesiano próprio:

- Origem (0,0) no canto superior esquerdo
- Eixo X cresce para a direita
- Eixo Y cresce para baixo

Para mapas astrais, criaremos um sistema **centrado no meio do canvas**.

---

## Módulo 2 – Matemática Angular Aplicada

### 2.1 Graus e Radianos

Astrologia trabalha em graus (0°–360°).
O Canvas trabalha em radianos.

Fórmula de conversão:

graus × π / 180

Essa conversão é obrigatória para qualquer cálculo gráfico.

### 2.2 Ajuste de Orientação Astrológica

No Canvas:
- 0 radianos aponta para a direita (leste)

No mapa astral:
- O Ascendente fica à esquerda
- O zodíaco gira no sentido anti-horário

Por isso aplicamos uma rotação de -90° ao converter ângulos.

---

## Módulo 3 – Estrutura do Zodíaco

### 3.1 Os 12 Signos

O círculo zodiacal possui:
- 360° totais
- 12 signos
- Cada signo ocupa exatamente 30°

Ordem zodiacal:
Áries → Touro → Gêmeos → Câncer → Leão → Virgem →
Libra → Escorpião → Sagitário → Capricórnio → Aquário → Peixes

### 3.2 Desenho dos Setores

Cada signo é representado como um setor circular.
Visualmente, o círculo é dividido em 12 fatias iguais.

---

## Módulo 4 – Casas Astrológicas (Placidus)

### 4.1 O que são Cúspides

As casas representam áreas da vida.
Diferente dos signos, **as casas não têm tamanho fixo**.

Elas são calculadas astronomicamente e variam conforme:
- Latitude
- Hora
- Data
- Sistema de casas

Neste curso utilizamos o sistema **Placidus**.

### 4.2 Cúspides Utilizadas

As cúspides reais usadas no projeto são:

Casa 1: 82.70°  
Casa 2: 111.13°  
Casa 3: 141.35°  
Casa 4: 173.62°  
Casa 5: 205.74°  
Casa 6: 235.36°  
Casa 7: 262.70°  
Casa 8: 291.13°  
Casa 9: 321.35°  
Casa 10: 353.62°  
Casa 11: 25.74°  
Casa 12: 55.36°  

Esses valores são usados diretamente no desenho.

---

## Módulo 5 – Planetas e Pontos Sensíveis

### 5.1 Corpos Celestes

O mapa inclui os seguintes corpos:

- Sol
- Lua
- Mercúrio
- Vênus
- Marte
- Júpiter
- Saturno
- Urano
- Netuno
- Plutão

Cada planeta possui uma longitude absoluta (0°–360°).

### 5.2 Posicionamento Gráfico

Os planetas são desenhados:
- Em um raio interno
- Sobrepostos ao círculo das casas
- Com espaçamento visual para evitar colisões

Cada planeta é tratado como um ponto polar convertido em coordenadas XY.

---

## Módulo 6 – Aspectos Astrológicos

### 6.1 O que são Aspectos

Aspectos são relações angulares entre planetas.
Eles indicam interação simbólica entre energias.

Aspectos principais usados:
- Conjunção (0°)
- Sextil (60°)
- Quadratura (90°)
- Trígono (120°)
- Oposição (180°)

Cada aspecto admite uma margem de erro (orbe).

### 6.2 Cálculo da Diferença Angular

Para identificar aspectos, calculamos a menor distância angular entre dois planetas,
sempre no intervalo de 0° a 180°.

---

## Módulo 7 – Camadas do Desenho

### 7.1 Ordem Correta de Renderização

Para um mapa limpo e profissional, desenhamos em camadas:

1. Fundo
2. Círculo externo
3. Signos
4. Casas
5. Aspectos
6. Planetas
7. Textos

Essa ordem evita sobreposição incorreta.

### 7.2 Refinamento Visual

Utilizamos:
- Espessuras diferentes de linha
- Transparência nos aspectos
- Fonte simples e legível

O foco é clareza, não excesso decorativo.

---

## Módulo 8 – Projeto Final

### 8.1 Resultado Obtido

Ao final do curso, o aluno possui:

- Um mapa astral completo em Canvas
- Código organizado e extensível
- Base sólida para:
  - Exportação em PDF
  - Aplicação desktop (Electron)
  - Integração com Swiss Ephemeris
  - Trânsitos e progressões

### 8.2 Próximos Passos

Sugestões de evolução:
- Uso de glifos astrológicos profissionais
- Cálculo astronômico em tempo real
- Interface interativa
- Impressão em A4

---

## Conclusão

Este curso une programação, matemática e astrologia de forma prática.
Mais do que gerar um gráfico, ele ensina **como pensar e construir um sistema gráfico completo**.

O aluno termina capaz de:
- Ler dados astronômicos
- Convertê-los em geometria
- Representar simbolicamente um mapa astral

---

Fim da Apostila
