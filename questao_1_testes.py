from questao_1_funcoes import *


# Validação do nome
print("Validação do nome")
nomes = ['Ada Lovelace', 'Alan Turing', 'Stephen Cole Kleene', '1Alan', 'Alan', 'A1an', 'Alan turing', 'A1an Turing']
for nome in nomes:
    print(f'Nome: {nome.ljust(20)} - Válido: {validar_nome(nome)}')
print()


# Validação do email
print("Validação do email")
emails = ['a@a.br', 'divulga@ufpa.br', 'a@a.com.br', '@', 'a@.br', '@a.br', 'T@teste.br', 'a@A.com.br', 'teste.a@ufpa.com']
for email in emails:
    print(f'Email: {email.ljust(20)} - Válido: {validar_email(email)}')
print()


# Validação da senha
print("Validação do senha")
senhas = ['518R2r5e', 'F123456A', '1234567T', 'ropsSoq0', 'F1234567A', 'abcdefgH', '1234567HI', 'aG9089']
for senha in senhas:
    print(f'Senha: {senha.ljust(20)} - Válido: {validar_senha(senha)}')
print()


# Validação do cpf
print("Validação do cpf")
cpfs = ['123.456.789-09', '000.000.000-00', '123.456.789-0', '111.111.11-11', '11109078645', '345876129-00', '098.678.12390']
for cpf in cpfs:
    print(f'CPF: {cpf.ljust(20)} - Válido: {validar_cpf(cpf)}')
print()


# Validação do telefone
print("Validação do telefone")
telefones = ['(91) 99999-9999', '(91) 999999999', '91 999999999', '(91) 59999-9999', '99 99999-9999', '(94)95555-5555']
for telefone in telefones:
    print(f'Telefone: {telefone.ljust(20)} - Válido: {validar_telefone(telefone)}')
print()


# Validação da data e da hora
print("Validação do data e da hora")
datas = ['31/08/2019 20:14:55', '99/99/9999 23:59:59', '99/99/9999 3:9:9', '9/9/99 99:99:99', '99/99/999903:09:09', '9/99/9999 3:09:09', '99/9/9999 03:9:09', '99/99/99 03:09:9', '99999999 03:09:09','99/99/9999 030909',]
for data in datas:
    print(f'Data e hora: {data.ljust(20)} - Válido: {validar_data_hora(data)}')
print()


# Validação do numero real
print("Validação do numero real")
numeros = ['1', '-1', '+1', '1.1', '-25.90', '0.2', '64.2', '1.', '.2', '+64,2']
for numero in numeros:
    print(f'Numero real: {numero.ljust(20)} - Válido: {validar_real(numero)}')
print()
