from questao_2_funcoes import arranjo_letra_g

# Lista contendo as cadeias para teste da expressão da letra G)
familias_teste = [
    ["M", 1, 1],        # Válido
    ["H", 1, 1],        # Válido
    ["H", 1, 2],        # Válido
    ["MH", 1, 2],       # Válido
    ["MHH", 1, 3],      # Válido
    ["MMH", 2, 3],      # Válido
    ["MMMM", 2, 4],     # Válido
    ["MHH", 2, 4],      # Válido
    ["MHHHH", 3, 5],    # Válido
    ["MHHHh", 1, 4],    # Válido
    ["MHMHhh", 2, 5],   # Válido
    ["MMm", 2, 5],      # Válido
    ["MHMhm", 1, 3],    # Válido
    ["MHmmhmm", 1, 4],  # Válido
    ["MM", 2, 2],       # Válido
    ["MHH", 2, 3],      # Válido
    ["Hh", 1, 2],       # Válido
    ["MHhh", 1, 3],     # Válido
    ["Mmh", 1, 2],      # Válido
    ["Mm", 1, 1],       # Válido
    ["MMm", 2, 3],      # Válido
    ["MMHhmh", 2, 5],   # Válido
    ["MHHhm", 2, 5],    # Válido
    ["MMmh", 2, 4],     # Válido
    ["HHm", 2, 3],      # Válido
    ["HHhh", 2, 4],     # Válido
    ["MMMhhhhm", 3, 5], # Válido
    ["Mhhhm", 1, 5],    # Válido
    ["MHh", 1, 3],      # Válido
    ["Mh", 1, 2],       # Válido
    ["MMMh", 3, 4],     # Válido
    ["MMhm", 2, 3],     # Válido
    ["Hhm", 1, 2],      # Válido
    ["M", 0, 1],        # Inválido (x não pode ser 0)
    ["M", 1, 0],        # Inválido (y não pode ser 0 nem menor que x)
    ["", 0, 0],         # Inválido (x e y não podem ser 0)
    ["MHmh", 2, 1],     # Inválido (y não pode ser nem menor que x)
    ["MMhhh", 2, 5],    # Inválido (Terminda com 3 filhos homens)
    ["MHhhh", 2, 5],    # Inválido (Terminda com 3 filhos homens)
    ["MMhhh", 2, 5],    # Inválido (Terminda com 3 filhos homens)
    ["Hhhh", 1, 4],     # Inválido (Terminda com 3 filhos homens)
    ["MHmhh", 1, 1],    # Inválido (Número de pais fora do intervalo de x e y)
    ["MMHhm", 4, 5],    # Inválido (Número de pais fora do intervalo de x e y)
    ["Mhmhh", 2, 5],    # Inválido (Número de pais fora do intervalo de x e y)
    ["Hhmh", 2, 5],     # Inválido (Número de pais fora do intervalo de x e y)
    ["MHHhhh", 2, 5],   # Inválido (Termina com 3 filhos homens)
    ["Mhhh", 1, 4],     # Inválido (Termina com 3 filhos homens)
]

# Laço para iterar sobre a lista de cadeias e mostrar quais são válidas ou não
for familia, x, y in familias_teste:
    print(f'Família: {familia.ljust(30)} - Válido: {arranjo_letra_g(familia, x, y)}')
print()
