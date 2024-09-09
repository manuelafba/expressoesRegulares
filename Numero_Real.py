import re 

expressao_num_real = re.compile(r'^[+-]?[0-9]+(\.[0-9]+)?$')

while(True):
    expresao_num_usuario = input('Insira aqui sua expressão:')
    validador_num_real = re.fullmatch(expressao_num_real, expresao_num_usuario)
    if (validador_num_real is None):
        print('Expressão inválida')
    else:
        print(f'Sua expressão "{expresao_num_usuario}" é válida')
        break

