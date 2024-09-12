from questao_1_funcoes import validar_email

emails_teste = [
    "joao@empresa.com.br",              # Válida
    "maria@dominio.br",                 # Válida
    "teste@provedor.com.br",            # Válida
    "exemplo@abc.br",                   # Válida
    "fulano@servico.com.br",            # Válida
    "jose@site.com.br",                 # Válida
    "alice@projeto.br",                 # Válida
    "pedro@negocio.com.br",             # Válida
    "lucas@empresa.br",                 # Válida
    "carlos@portal.com.br",             # Válida
    "joao@com.br",                      # Válida
    "a@b.br",                           # Válida
    "JOAO@empresa.com.br",              # Inválida (letras maiúsculas não permitidas)
    "joao@empresa.com",                 # Inválida (terminação inválida)
    "joao.empresa@com.br",              # Inválida (ponto antes do @)
    "joao@empresa@com.br",              # Inválida (dois @)
    "joao@empresa..com.br",             # Inválida (dois pontos seguidos)
    "joaoempresa.com.br",               # Inválida (falta o @)
    "@empresa.com.br",                  # Inválida (falta letras antes do @)
    "joao@.com.br",                     # Inválida (falta letras antes de .com.br)
    "joao@empresa.com.com.br",          # Inválida (extra ".com")
    "joao@empresa.org.br",              # Inválida (domínio .org não permitido)
    "joao@empresa.br.br",               # Inválida (repetição de .br)
    "joaonumeros123@empresa.com.br",    # Inválida (contém números antes do @)
    "joao@numeros123.com.br",           # Inválida (contém números após o @)
    "_joao@empresa.com.br",             # Inválida (caracteres especiais antes do @)
    "joao@empresa_123.com.br",          # Inválida (contém caracteres especiaise e números no domínio)
    "joao@empresa.com.br123",           # Inválida (números após .br)
    "joao@empresa",                     # Inválida (sem final .com.br ou .br)
    "joao@empresa.c",                   # Inválida (domínio incorreto)
    "joao@com",                         # Inválida (falta o domínio .br)
    "joao@empresa..br",                 # Inválida (dois pontos seguidos)
    "joao@empresa_com.br",              # Inválida (tem underline)
    "joao@empresa.co",                  # Inválida (terminação errada, falta m.br)
    "@com.br",                          # Inválida (falta domínio antes do @)
    ".joao@empresa.com.br",             # Inválida (ponto antes do nome de usuário)
    "joao@empresa@com.br",              # Inválida (dois @)
    "joao@empresa.br..",                # Inválida (dois pontos após .br)
    "joao@br.com",                      # Inválida (faltou o .br)
    "joao@dominio.c",                   # Inválida (terminação errada, falta om.br)
    "joao@dominio.a.b.c.br",            # Inválida (vários . antes da terminação .br)
    "abcde@fghij@k.com.br",             # Inválida (dois @)
    "@@@@empresa.com.br",               # Inválida (mais de um @)
    "abc@@empresa.com.br",              # Inválida (dois @)
    "abc.@empresa.com.br",              # Inválida (ponto antes do @)
    "abc@.com.br",                      # Inválida (ponto logo após o @)
    "abc@dominio..com.br",              # Inválida (dois pontos seguidos)
    "a@com",                            # Inválida (domínio incompleto)
    "usuario@domaincombr",              # Inválida (falta o ponto antes de com.br)
    "usuario@domain.com"                # Inválida (faltando o .br no final)
]

for email in emails_teste:
    print(f'Email: {email.ljust(30)} - Válido: {validar_email(email)}')
print()
