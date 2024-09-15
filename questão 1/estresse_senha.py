from questao_1_funcoes import validar_senha

# Lista contendo as cadeias para teste da expressão regular da máscara de validação de senha
senhas_teste = [
    "518R2r5e",    # Válida
    "F123456A",    # Válida
    "1234567T",    # Válida
    "ropsSoq0",    # Válida
    'Abcdef12',    # Válida
    'abcDef12',    # Válida
    'ABcdef34',    # Válida    
    'A1bcdefg',    # Válida
    'aBcdef67',    # Válida
    'aB1cdEfg',    # Válida
    'xyZ12345',    # Válida
    'MN1opqRS',    # Válida
    'AbcD1eF2',    # Válida
    'xyzABC12',    # Válida
    '1AaBbCcD',    # Válida
    'XyZ12abc',    # Válida
    'C3D4eF5g',    # Válida
    'mnopQR78',    # Válida
    'ABC12345',    # Válida
    '1111AAAA',    # Válida
    'AbcdEfgh',    # Inválida (Não tem número)
    'AaBbCcDd',    # Inválida (Não tem número)
    'A1bcdef',     # Inválida (Tem menos de 8 caracteres)
    'abcdefgh',    # Inválida (Não tem maiúscula e número)
    'ABCDEFGH',    # Inválida (Não tem número)
    '12345678',    # Inválida (Não tem maiúscula)
    'HijklMno',    # Inválida (Não tem número)
    'abcdefgh',    # Inválida (Não tem maiúscula e número)
    '1234abcd',    # Inválida (Não tem maiúscula)
    'abcdEFG1kjl', # Inválida (Tem mais de 8 caracteres)
    '!@#$%&*&' ## Inválida (Caracteres especiais)
]

# Laço para iterar sobre a lista de cadeias e mostrar quais são válidas ou não
for senha in senhas_teste:
    print(f'Senha: {senha.ljust(30)} - Válido: {validar_senha(senha)}')
print()
