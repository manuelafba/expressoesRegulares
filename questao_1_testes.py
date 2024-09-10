from questao_1_funcoes import *

# Mensagem de boas-vindas
print("Bem-vindo ao programa de validação de cadastro!!!")
print("Vamos iniciar o cadastro")

# Validação do nome
print("""
Digite o nome. Ele deve possuir primeiro e último nome, nomes intermediários são opcionais.
Cada nome deve começar com uma letra maiúscula e ser seguido por letras minúsculas.
Não devem conter símbolos nem números.\n""")

while True:
    tentativa_nome = input("Digite aqui o seu nome: ")
    resultado = validar_nome(tentativa_nome)
    if not resultado:
        print("Nome inválido, tente novamente\n")
    else:
        print("Nome válido\n")
        break

# Validação do email
print("""
Digite seu email. Ele deve conter apenas um '@', uma ou mais letras minúsculas antes e depois do '@',
possuir apenas letras minúsculas e terminar com '.com.br' ou '.br'.\n""")

while True:
    tentativa_email = input("Digite aqui o seu email: ")
    resultado = validar_email(tentativa_email)
    if not resultado:
        print("Email inválido, tente novamente\n")
    else:
        print("Email válido\n")
        break

# Validação da senha
print("""
Digite sua senha. Ela pode conter apenas letras maiúsculas, minúsculas e números.
Deve conter pelo menos uma letra maiúscula, uma letra minúscula e ter no mínimo 8 caracteres.\n""")

while True:
    tentativa_senha = input("Digite aqui a sua senha: ")
    resultado = validar_senha(tentativa_senha)
    if not resultado:
        print("Senha inválida, tente novamente\n")
    else:
        print("Senha válida\n")
        break

# Validação do CPF
print("""
Digite o seu CPF. Ele deve ter o formato xxx.xxx.xxx-xx, com 'x' sendo números.\n""")

while True:
    tentativa_cpf = input("Digite aqui o seu CPF: ")
    resultado = validar_cpf(tentativa_cpf)
    if not resultado:
        print("CPF inválido, tente novamente\n")
    else:
        print("CPF válido\n")
        break

# Validação do telefone
print("""
Digite o seu número de telefone. Ele deve ter um dos seguintes formatos:
  (xx) 9xxxx-xxxx
  (xx) 9xxxxxxxx
  xx 9xxxxxxxx
com 'x' sendo números.\n""")

while True:
    tentativa_telefone = input("Digite aqui o seu telefone: ")
    resultado = validar_telefone(tentativa_telefone)
    if not resultado:
        print("Telefone inválido, tente novamente\n")
    else:
        print("Telefone válido\n")
        break

# Validação da data e horário
print("""
Digite a sua data e horário no formato dd/mm/aaaa hh:mm:ss, onde d, m, a, h, m, s são números.\n""")

while True:
    tentativa_data = input("Digite aqui a sua data e horário: ")
    resultado = validar_data(tentativa_data)
    if not resultado:
        print("Data inválida, tente novamente\n")
    else:
        print("Data válida\n")
        break

# Validação do número real
print("""
Por fim, digite o seu número real. Ele deve seguir as seguintes regras:
  1. Começar com um dos símbolos {+, -, ε}.
  2. Seguir com, pelo menos, um número.
  3. Ter exatamente um símbolo separador “.”.
  4. Finalizar com, pelo menos, um número.
  5. Exceção: números sem a parte fracionária também são aceitos.\n""")

while True:
    tentativa_real = input("Digite aqui o seu número real: ")
    resultado = validar_real(tentativa_real)
    if not resultado:
        print("Número real inválido, tente novamente\n")
    else:
        print("Número real válido\n")
        break

# Finalização do cadastro
print(f"""
Cadastro finalizado! Seus dados são:
  Nome: {tentativa_nome}
  Email: {tentativa_email}
  Senha: {tentativa_senha}
  CPF: {tentativa_cpf}
  Telefone: {tentativa_telefone}
  Data e hora: {tentativa_data}
  Número Real: {tentativa_real}
""")
