from questao_1_funcoes import validar_cpf

# Lista contendo as cadeias para teste da expressão regular da máscara de validação de nome
cpfs_teste = [
    "123.456.789-00", # Válido
    "111.222.333-44", # Válido
    "987.654.321-99", # Válido
    "123.456.789-01", # Válido
    "000.000.000-01", # Válido
    "000.000.000-00", # Válido 
    "999.999.999-99", # Válido 
    "123.456.789-12", # Válido
    "234.567.890-23", # Válido
    "345.678.901-34", # Válido
    "456.789.012-45", # Válido
    "567.890.123-56", # Válido
    "678.901.234-67", # Válido
    "789.012.345-78", # Válido
    "890.123.456-89", # Válido
    "901.234.567-90", # Válido
    "012.345.678-01", # Válido
    "12345678900",    # Inválido (sem pontos e hífen)
    "123.456.789-000",# Inválido (dois dígitos a mais no final)
    "123.456.78-90",  # Inválido (um dígito a menos)
    "123.456.7890-12",# Inválido (dígito a mais)
    "12.345.678-90",  # Inválido (dígito a menos)
    "123.456.78-901", # Inválido (padrão errado no final xx-xxx)
    "123.456.78-9a",  # Inválido (caractere não numérico)
    "abc.def.ghi-jk", # Inválido (não é numérico)
    "123-456-789-00", # Inválido (hífen no lugar dos pontos)
    "123.456.78-00",  # Inválido (um dígito a menos antes do hífen)
    "123.456.789-0a", # Inválido (letra no final)
    "123-456-789-01", # Inválido (hífen no lugar dos pontos)
    "123.456.789-001",# Inválido (dígitos extra no final)
    "123.4567.89-01", # Inválido (blocos de dígitos não estão corretos)
    "123.456.789-0",  # Inválido (dígito a menos)
    "1234.567.890-12",# Inválido (dígitos a mais no início)
    "12.3456.789-01", # Inválido (blocos de dígitos não estão corretos)
    "123.45.678-90",  # Inválido (dígito a menos)
    "123.456.78-9012",# Inválido (dígitos extras no final)
    "12.345.67890-12",# Inválido (falta um ponto)
]

# Laço para iterar sobre a lista de cadeias e mostrar quais são válidas ou não
for cpf in cpfs_teste:
    print(f'CPF: {cpf.ljust(30)} - Válido: {validar_cpf(cpf)}')
print()
