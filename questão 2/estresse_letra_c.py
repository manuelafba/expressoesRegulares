from questao_2_funcoes import arranjo_letra_c

# Lista contento as cadeias para teste da expressão da letra C)
familias_teste = [
    "MH",           # Válido
    "HM",           # Válido
    "MHmh",         # Válido
    "MHmmmh",       # Válido
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
    "MHhhhh",       # Inválido (Somente filhos)
    "HMhmmhh",      # Inválido (Mais velho e mais novo homem)
    "MHmmhm",       # Inválido (Mais velho e mais novo mulher)
    "HMhmhmh",      # Inválido (Mais velho e mais novo homem)
    "HMhhh",        # Inválido (Somente filhos)
    "MHmm",         # Inválido (Somente filhas)
    "HMmhm",        # Inválido (Mais velho e mais novo mulher)
    "MHhmhm",       # Inválido (Mais velho homem e mais novo mulher)
    "HMhhmh",       # Inválido (Mais velho e mais novo homem)
    "HMhmmm",       # Inválido (Mais velho homem e mais novo mulher)
    "HMhmh",        # Inválido (Mais velho e mais novo homem)
    "MHhmm",        # Inválido (Mais velho homem e mais novo mulher)
    "HMmmm",        # Inválido (Somente filhas)
    "MHmmmm",       # Inválido (Somente filhas)
    "HMmmhmm",      # Inválido (Mais velho e mais novo mulher)
    "MHhmh",        # Inválido (Mais velho e mais novo homem)
    "MHmhmmm",      # Inválido (Mais velho e mais novo mulher)
    "HMhhhh",       # Inválido (Somente filhos)
    "MHhmhh",       # Inválido (Mais velho e mais novo homem)
    "HMhhmm",       # Inválido (Mais velho homem e mais novo mulher)
    "HMhmmmh",      # Inválido (Mais velho e mais novo homem)
    "MHmhmhm",      # Inválido (Mais velho e mais novo mulher)
    "HMmmmhm",      # Inválido (Mais velho e mais novo mulher)
    "MHhmhmh",      # Inválido (Mais velho e mais novo homem)
    "HMmhmhm",      # Inválido (Mais velho e mais novo mulher)
    "HMhmhhm"       # Inválido (Mais velho homem e mais novo mulher)
]

# Laço para iterar sobre a lista de cadeias e mostrar quais são válidas ou não
for familia in familias_teste:
    print(f'Família: {familia.ljust(30)} - Válido: {arranjo_letra_c(familia)}')
print()
