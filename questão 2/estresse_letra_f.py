from questao_2_funcoes import arranjo_letra_f

# Lista contendo as cadeias para teste da expressão da letra F)
familias_teste = [
    "HHm",     # Válido
    "MMh",     # Válido
    "HHmh",    # Válido
    "MMmh",    # Válido
    "HHmhm",   # Válido
    "MMmhmh",  # Válido
    "HH",      # Válido
    "MM",      # Válido
    "HHh",     # Válido
    "MMmhmm",  # Válido
    "HHmhmm",  # Válido
    "MMm",     # Válido
    "HHmhmhm", # Válido
    "HHhm",    # Válido
    "HHhmh",   # Válido 
    "HHhh",    # Inválido (dois filhos homens consecutivos)
    "MMhh",    # Inválido (dois filhos homens consecutivos)
    "HHhhm",   # Inválido (dois filhos homens consecutivos)
    "HHhhhh",  # Inválido (dois filhos homens consecutivos)
    "MMmhh",   # Inválido (dois filhos homens consecutivos)
    "HHhhhhm", # Inválido (dois filhos homens consecutivos)
    "MMmhhhhm",# Inválido (dois filhos homens consecutivos)
    "HHhhmhm", # Inválido (dois filhos homens consecutivos)
    "MMhhh",   # Inválido (dois filhos homens consecutivos)
    "HHhmhh",  # Inválido (dois filhos homens consecutivos)
    "MMhmhh",  # Inválido (dois filhos homens consecutivos)
    "MMhhhh",  # Inválido (dois filhos homens consecutivos)
    "HHhhmm",  # Inválido (dois filhos homens consecutivos)
    "HMhmm",   # Inválido (Casal hetero)
    "MHhmhmhm" # Inválido (Casal hetero)
]

# Laço para iterar sobre a lista de cadeias e mostrar quais são válidas ou não
for familia in familias_teste:
    print(f'Família: {familia.ljust(30)} - Válido: {arranjo_letra_f(familia)}')
print()
