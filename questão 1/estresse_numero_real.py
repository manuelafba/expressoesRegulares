from questao_1_funcoes import validar_real

# Lista contendo as cadeias para teste da expressão regular da máscara de validação de número real
numeros_teste = [
    "+123.456",         # Válido
    "-123.456",         # Válido
    "123.456",          # Válido
    "+123",             # Válido
    "-123",             # Válido
    "123",              # Válido
    "+0.123",           # Válido
    "-0.123",           # Válido
    "0.123",            # Válido
    "+0",               # Válido
    "-0",               # Válido
    "0",                # Válido
    "0.0",              # Válido
    "000.123",          # Válido 
    "+000.123",         # Válido
    "-000.123",         # Válido
    ".456",             # Inválido (falta número antes do .)
    "+.0",              # Inválido (falta número antes do .)
    "-.0"               # Inválido (falta número antes do .)
    "+.456",            # Inválido (falta número antes do .)
    "456.",             # Inválido (falta número depois do .)
    "+456.",            # Inválido (falta número depois do .)
    "1.",               # Inválido (falta número depois do .)
    "0.",               # Inválido (falta número depois do .)
    "123abc",           # Inválido (contém letras)
    "1.23.45",          # Inválido (contém mais de um .)
    "12..34",           # Inválido (contém mais de um .)
    "12.34.",           # Inválido (contém mais de um .)
    "-123.45.6",        # Inválido (contém mais de um .)
    "+123.45.6",        # Inválido (contém mais de um .)
    ".12.",             # Inválido (contém mais de um .)
    "++123",            # Inválido (contém mais de um +)
    "--123",            # Inválido (contém mais de um -)
    "12-34",            # Inválido (contém + no meio do número)
    "12+34",            # Inválido (contém - no meio do número)
    "+-.123",           # Inválido (contém + e -)
    "-+0.123",          # Inválido (contém + e -)
    "123 456",          # Inválido (contém espaço)
]

# Laço para iterar sobre a lista de cadeias e mostrar quais são válidas ou não
for numero in numeros_teste:
    print(f'Número real: {numero.ljust(30)} - Válido: {validar_real(numero)}')
print()
