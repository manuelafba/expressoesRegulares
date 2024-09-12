from questao_1_funcoes import validar_senha

senhas_teste = [
    'Abcdef12',    # Válida
    'abcDef12',    # Válida
    'ABcdef34',    # Válida    
    'A1bcdefg',    # Válida
    'aBcdef67',    # Válida
    '1Abcdefg',    # Válida
    'A2345678',    # Válida    
    'ABC12def',    # Válida
    'Abc1deFg',    # Válida
    '1234Abcd',    # Válida
    'abcdefG1',    # Válida
    '1a2b3C4d',    # Válida 
    '123456Ab',    # Válida
    'Z1x2c3V4',    # Válida   
    'A1b2c3de',    # Válida
    'zZ123456',    # Válida
    '1a2b3cDE',    # Válida
    'Q1w2e3R4',    # Válida
    'S1t2u3V4',    # Válida
    'aB1cdEfg',    # Válida
    'xyZ12345',    # Válida
    'MN1opqRS',    # Válida
    'AbcD1eF2',    # Válida
    'xyzABC12',    # Válida
    '1AaBbCcD',    # Válida
    'XyZ12abc',    # Válida
    'A1234def',    # Válida
    'abcdefG7',    # Válida
    'Zyx12345',    # Válida
    'QwErTy12',    # Válida
    'aA1bB2cC',    # Válida
    'X1y2Z3a4',    # Válida
    'AaBbCc12',    # Válida
    'G7abcdef',    # Válida
    'C3D4eF5g',    # Válida
    'mnopQR78',    # Válida
    'ABC12345',    # Válida
    '1111AAAA',    # Válida
    'AbcdEfgh',    # Inválida (sem número)
    'AaBbCcDd',    # Inválida (sem número)
    'A1bcdef',     # Inválida (menos de 8 caracteres)
    'abcdefgh',    # Inválida (sem maiúscula e número)
    'ABCDEFGH',    # Inválida (sem número)
    '12345678',    # Inválida (sem maiúscula)
    'HijklMno',    # Inválida (sem número)
    'abcdefgh',    # Inválida (sem maiúscula e número)
    '1234abcd',    # Inválida (sem maiúscula)
    'abcdEFG1kjl', # Inválida (comprimento maior que 8)
]


for senha in senhas_teste:
    print(f'Senha: {senha.ljust(30)} - Válido: {validar_senha(senha)}')
print()
