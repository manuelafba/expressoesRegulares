from questao_2_funcoes import arranjo_letra_c

# Lista contendo as cadeias para teste da expressão da letra C)
familias_teste = [
    "MH",           # Válido
    "HM",           # Válido
    "MHmh",         # Válido
    "HMmmhh",       # Válido 
    "MHmmmmmh",     # Válido  
    "MHmmh",        # Válido
    "MHmhh",        # Válido
    "HMmmmmh",      # Válido
    "HMmh",         # Válido
    "MHmmhmh",      # Válido
    "MHmhmmh",      # Válido
    "HMmhmmh",      # Válido
    "MHmhmh",       # Válido
    "MHmhmhh",      # Válido
    "MHm",          # Inválido (Somente uma filha)
    "HMh",          # Inválido (Somente um filho)
    "HHmmh",        # Inválido (Casal homo)
    "HMhm",         # Inválido (Mais velho homem e mais nova mulher)
    "HMhmhm",       # Inválido (Mais velho homem e mais nova mulher)
    "MMmmmh",       # Inválido (Casal homo)
    "MHhhhhh",      # Inválido (Somente filhos)
    "HMhmmhh",      # Inválido (Mais velho e mais novo homem)
    "MHmmhm",       # Inválido (Mais velho e mais novo mulher)
    "HMhmhmh",      # Inválido (Mais velho e mais novo homem)
    "HMhhh",        # Inválido (Somente filhos)
    "MHmm",         # Inválido (Somente filhas)
    "HMmhm",        # Inválido (Mais velho e mais novo mulher)
    "HMhhmh",       # Inválido (Mais velho e mais novo homem)
    "HMhmmm",       # Inválido (Mais velho homem e mais nova mulher)
    "HMmmm",        # Inválido (Somente filhas)
]

# Laço para iterar sobre a lista de cadeias e mostrar quais são válidas ou não
for familia in familias_teste:
    print(f'Família: {familia.ljust(30)} - Válido: {arranjo_letra_c(familia)}')
print()
