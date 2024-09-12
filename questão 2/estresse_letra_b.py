from questao_2_funcoes import arranjo_letra_b

# Lista contento as cadeias para teste da expressão da letra B)
familias_teste = [
    "MHmhmhm",      # Válido
    "HMhmhmhmh",    # Válido
    "HMhhhhm",      # Válido
    "MHhm",         # Válido
    "HMhmh",        # Válido
    "MHmh",         # Válido
    "MHhmhmhmh",    # Válido
    "MHmh",         # Válido
    "MHhhhhhm",     # Válido
    "HMmhmhm",      # Válido
    "MHhmh",        # Válido
    "HMhmh",        # Válido
    "MHhmhmhmhmhm", # Válido
    "MHhmhmhm",     # Válido
    "HMhmhmhm",     # Válido
    "MHhmhmhmhmhm", # Válido
    "MHhhhm",       # Válido
    "MHmhhmh",      # Inválido (Número par de filhas)
    "HMhmhm",       # Inválido (Número par de filhas)
    "MHhmhmh",      # Inválido (Número par de filhas)
    "HMh",          # Inválido (Número par de filhas)
    "MHhhhh",       # Inválido (Número par de filhas)
    "HMhhhh",       # Inválido (Número par de filhas)
    "MH",           # Inválido (Número par de filhas)
    "HM",           # Inválido (Número par de filhas)
    "HMhmhmhmhm",   # Inválido (Número par de filhas)
    "HMhmhmh",      # Inválido (Número par de filhas)
    "MHhmhmhmhmh",  # Inválido (Número par de filhas)
    "HMhhhhhh",     # Inválido (Número par de filhas)
    "HMhmhm",       # Inválido (Número par de filhas)
    "MHhmhmh",      # Inválido (Número par de filhas)
    "MHmhmhmhmh",   # Inválido (Número par de filhas)
    "HM",           # Inválido (Número par de filhas)
    "HMhhhh",       # Inválido (Número par de filhas)
    "MHmhmh",       # Inválido (Número par de filhas)
    "HMh",          # Inválido (Número par de filhas)
    "MH",           # Inválido (Número par de filhas)
    "HMhmm",        # Inválido (Número par de filhas)
    "HM",           # Inválido (Número par de filhas)
    "HHhmhmm",      # Inválido (Casal homo)
    "HMhmhmh",      # Inválido (Número par de filhas)
    "MHhmhmh",      # Inválido (Número par de filhas)
    "HMh",          # Inválido (Número par de filhas)
    "MHhmhmhmhm",   # Inválido (Número par de filhas)
    "HMhmhmhmhm",   # Inválido (Número par de filhas)
    "MHh",          # Inválido (Número par de filhas)
    "HM",           # Inválido (Número par de filhas)
    "MMhmhmhmh",    # Inválido (Casal homo)
    "MHhmhmhmhm",   # Inválido (Número par de filhas)
]

# Laço para iterar sobre a lista de cadeias e mostrar quais são válidas ou não
for familia in familias_teste:
    print(f'Família: {familia.ljust(30)} - Válido: {arranjo_letra_b(familia)}')
print()
