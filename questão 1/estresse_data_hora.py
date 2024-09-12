from questao_1_funcoes import validar_data_hora

# Lista contendo as cadeias para teste da expressão regular da máscara de validação de data e horário
data_horas_teste = [
    "01/01/2020 00:00:00",  # Válido
    "29/02/2024 23:59:59",  # Válido
    "31/12/1999 12:30:45",  # Válido
    "15/08/2021 14:15:30",  # Válido
    "10/06/2015 05:05:05",  # Válido
    "20/11/2000 20:20:20",  # Válido
    "25/07/2030 08:45:55",  # Válido
    "30/09/2022 09:09:09",  # Válido
    "01/03/1997 17:22:22",  # Válido
    "19/04/2025 18:00:00",  # Válido
    "2/01/2020 00:00:00",   # Inválido (formato do dia inválido)
    "29/2/2019 23:59:59",   # Inválido (formato do mes inválido)
    "31/04/20 12:30:45",    # Inválido (formato do ano inválido)
    "15/13/2021 7:15:30",   # Inválido (formato da hora inválida)
    "10/06/2015 24:5:05",   # Inválido (formato da hora inválida)
    "99/99/9999 99:99:1",   # Inválido (formato da hora inválida)
    "01012020 00:60:00",    # Inválido (sem /)
    "01/01/2020 000060",    # Inválido (sem :)
    "2020/01/01 00:00:00",  # Inválido (formato inválido)
    "01012003 000000",      # Inválido (sem / e :)
    "01/01/200300:00:00",   # Inválido (sem espaço )
    ]

# Laço para iterar sobre a lista de cadeias e mostrar quais são válidas ou não
for data_hora in data_horas_teste:
    print(f'Data e Hora: {data_hora.ljust(30)} - Válido: {validar_data_hora(data_hora)}')
print()
