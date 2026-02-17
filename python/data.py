"""Dados de exemplo: posições (longitude em graus) e cúspides.
Valores extraídos do esboço original para testes locais.
"""

BODIES = [
    {'code': 'sol', 'name': 'Sol', 'lon': 97.66258108350277},
    {'code': 'lua', 'name': 'Lua', 'lon': 307.45897771452724},
    {'code': 'mer', 'name': 'Mercúrio', 'lon': 120.93337502214607},
    {'code': 'ven', 'name': 'Vênus', 'lon': 80.14610622862499},
    {'code': 'mar', 'name': 'Marte', 'lon': 120.41815865545398},
    {'code': 'jup', 'name': 'Júpiter', 'lon': 272.8764596834747},
    {'code': 'sat', 'name': 'Saturno', 'lon': 73.65471642572109},
    {'code': 'ura', 'name': 'Urano', 'lon': 194.2188738028474},
    {'code': 'net', 'name': 'Netuno', 'lon': 243.00432631346524},
    {'code': 'plu', 'name': 'Plutão', 'lon': 179.42140571551036}
]

CUSPS = [
    82.70154304778679, 111.1341504020764, 141.3461512349346, 173.6225546549408,
    205.73919610408942, 235.36167285257102, 262.7015430477868, 291.1341504020764,
    321.3461512349346, 353.62255465494087, 25.73919610408942, 55.361672852571004
]

if __name__ == '__main__':
    print('BODIES sample:', BODIES)
    print('CUSPS sample:', CUSPS)
