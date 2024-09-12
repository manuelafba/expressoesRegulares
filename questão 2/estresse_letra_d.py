from questao_2_funcoes import arranjo_letra_d

# Lista contento as cadeias para teste da expressão da letra D)
familias_teste = [
    'MMmhhmhmmh',       # Válido 
    'MMhmhmmmhhmh',     # Válido
    'MMhmhmhm',         # Válido
    'MMmhhhmhm',        # Válido
    'HHhmhhmh',         # Válido
    'HHhmhhmhm',        # Válido 
    'HHmhmhmhmhmh',     # Válido 
    'HHmhhhhmh',        # Válido
    'HHhmhhhmmmmh',     # Válido
    'MMhmhhmhmmh',      # Válido
    'MMmhmmhm',         # Válido
    'MMmhhmhmmhmh',     # Válido
    'HHhmhmmhmmhm',     # Válido
    'MMhmmhhmh',        # Válido
    'HHmhhhmhmmh',      # Válido      
    'MMhmhhhmmhhm',     # Válido  
    'HHhmmmhmhhm',      # Válido
    'HHmhhhmmmmmh',     # Válido
    'MMmhhhhm',         # Válido
    'HHmhhhmh',         # Válido
    'MMmhhmhmmhhm',     # Válido
    'HHmhmhmmhhhm',     # Válido
    'HHhmmmhhm',        # Válido
    'MMhmmmmhm',        # Válido
    'MHhmhmmmhhhm',     # Inválido (Casal hetero)
    'HMhmhmhhm',        # Inválido (Casal hetero)
    'MMhmmhhmhh',       # Inválido (Finaliza com dois homens)
    'HHmhmmmm',         # Inválido (Finaliza com duas mulheres)
    'HHhhhhhmh',        # Inválido (Começa com dois homens)
    'HHmmhmmhhm',       # Inválido (Começa com duas mulheres)
    'MMmhmhm',          # Inválido (Menos que 6 filhos)
    'HHhmmh',           # Inválido (Menos que 6 filhos)
    'HH',               # Inválido (Nenhum filho)
    'MM',               # Inválido (Nenhum filho)
]

# Laço para iterar sobre a lista de cadeias e mostrar quais são válidas ou não
for familia in familias_teste:
    print(f'Família: {familia.ljust(30)} - Válido: {arranjo_letra_d(familia)}')
print()
