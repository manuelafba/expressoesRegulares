import re

expressao_data_hora = re.compile(r'^[0-9]{2}/[0-9]{2}/[0-9]{4}\s[0-9]{2}:[0-9]{2}:[0-9]{2}$')

while(True):
    expressao_usuario = input("Insira aqui sua expressão:")
    verificador = re.fullmatch(expressao_data_hora,expressao_usuario)
    if (verificador is None):
        print('Expressão inválida')
    else:
        print(f'Sua expressão "{expressao_usuario}" é válida')
        break
