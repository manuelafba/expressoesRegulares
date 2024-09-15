from questao_1_funcoes import validar_telefone

# Lista contendo as cadeias para teste da expressão regular da máscara de validação de telefone
telefones_teste = [
    "(11) 91234-5678",  # Válido
    "(22) 912345678",   # Válido
    "31 912345678",     # Válido
    "(44) 934567890",   # Válido
    "55 934567890",     # Válido
    "(99) 91234-5678",  # Válido
    "12 999999999",     # Válido
    "(23) 955555555",   # Válido
    "55 955555555",     # Válido
    "(71) 99999-1111",  # Válido
    "99 988887777",     # Válido
    "21 922223333",     # Válido
    "(35) 99999-8888",  # Válido
    "99 987654321",     # Válido
    "(66) 98765-4321",  # Válido
    "(12)  94567-8901", # Inválido (espaço extra entre o DDD e o 9)
    "12  945678901",    # Inválido (espaço extra entre o DDD e o 9)
    "(12)  945678901",  # Inválido (espaço extra entre o DDD e o 9)
    "(81)91234-5678",   # Inválido (sem espaço após parênteses)
    "(12) 345678901",   # Inválido (não começa com 9)
    "12 345678901",     # Inválido (não começa com 9)
    "(22) 92345 6789",  # Inválido (espaço sem hífen)
    "(77) 9123456-789", # Inválido (dígitos a mais)
    "(35) 1234-5678",   # Inválido (faltando o 9)
    "12 93456789",      # Inválido (um dígito a menos)
    "123 912345678",    # Inválido (código de área com 3 dígitos)
    "(32) 91234-567",   # Inválido (um dígito a menos)
    "(21) 91234567890", # Inválido (dígitos a mais)
    "(41) 91-234-5678", # Inválido (hífen no lugar errado)
    "61-912345678",     # Inválido (hífen ao invés de espaço)
    "(62)9 1234-5678",  # Inválido (espaço depois do 9)
    "(34) 9912345678",  # Inválido (10 números)
    "54 9912345678",    # Inválido (10 números)
    "(71) 9912345678",  # Inválido (10 números)
    "(81) 9 1234-5678", # Inválido (espaço entre 9 e número)
    "(82) 9123-45678",  # Inválido (hífen no lugar errado)
    "(99) 9123-5678",   # Inválido (número a menos)
    "12 9 1234-5678",   # Inválido (espaço antes do 9)
    "(33) 99123456789", # Inválido (número a mais)
]

# Laço para iterar sobre a lista de cadeias e mostrar quais são válidas ou não
for telefone in telefones_teste:
    print(f'Telefone: {telefone.ljust(30)} - Válido: {validar_telefone(telefone)}')
print()
