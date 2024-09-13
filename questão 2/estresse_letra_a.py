from questao_2_funcoes import arranjo_letra_a

# Lista contendo as cadeias para teste da expressão da letra A)
familias_teste = [
    "MHhh",     # Válida
    "MHhm",     # Válida
    "MHmm",     # Válida
    "MHhhh",    # Válida  
    "MHmmmm",   # Válida  
    "HMhmm",    # Válida   
    "HMh",      # Válida  
    "HMhhm",    # Válida      
    "MHhmh",    # Válida  
    "MHhhmh",   # Válida  
    "MHhmhm",   # Válida  
    "MHhhhm",   # Válida  
    "HMmmhm",   # Válida  
    "HMhmhh",   # Válida  
    "HMmmhh",   # Válida  
    "MHhhhmm",  # Válida  
    "MHhmhmm",  # Válida  
    "MHmmhmm",  # Válida    
    "MHmhhhm",  # Válida  
    "MHmhhh",   # Válida 
    "HMhmhhh",  # Válida    
    "HMmmhhh",  # Válida   
    "HMhmhhm",  # Válida  
    "HMhhmmm",  # Válida 
    "MMhhmhm",  # Inválida (Casal homo)
    "HHmmhmh",  # Inválida (Casal homo)
    "MH",       # Inválida (Sem filhos)
    "HM",       # Inválida (Sem filhos)
    "MHm",      # Inválida (Só uma filha mulher)
    "HMm",      # Inválida (Só uma filha mulher)
]

# Laço para iterar sobre a lista de cadeias e mostrar quais são válidas ou não
for familia in familias_teste:
    print(f'Família: {familia.ljust(30)} - Válido: {arranjo_letra_a(familia)}')
print()
