from questao_2_funcoes import arranjo_letra_e

# Lista contendo as cadeias para teste da expressão da letra E)
familias_teste = [
    "MMmh",         # Válido
    "MMhm",         # Válido
    "HHmh",         # Válido
    "HHhm",         # Válido
    "MMmhmh",       # Válido
    "HHhmhm",       # Válido 
    "MMmhmhmh",     # Válido
    "HHhmhmhm",     # Válido
    "MMmhmhm",      # Válido
    "HHhmhmhmh",    # Válido 
    "HHhmhmhmhm",   # Válido
    "HHhmhmhmhmh",  # Válido
    "HHh",          # Válido
    "HHmhmhmhm",    # Válido
    "MMh",          # Válido
    "MM",           # Inválido (casal sem filhos)
    "HH",           # Inválido (casal sem filhos)
    "HHhmhmhmhh",   # Inválido (dois filhos seguidos)
    "HHhmhmmhmhm",  # Inválido (duas filhas seguidas)
    "MHhmhmhmhmh",  # Inválido (casal hetero)
    "HHhmm",        # Inválido (sem alternância do sexo dos filhos)
    "HMmhmhmhm",    # Inválido (casal hetero)
    "MMmmmmh",      # Inválido (sem alternância do sexo dos filhos)
    "HHhhhm",       # Inválido (sem alternância do sexo dos filhos)
    "MMhhmhmhh",    # Inválido (dois filhos seguidos)
    "HHhmhmmmhm",   # Inválido (três filhas seguidas)
    "HMm",          # Inválido (casal hetero)
]

# Laço para iterar sobre a lista de cadeias e mostrar quais são válidas ou não
for familia in familias_teste:
    print(f'Família: {familia.ljust(30)} - Válido: {arranjo_letra_e(familia)}')
print()
