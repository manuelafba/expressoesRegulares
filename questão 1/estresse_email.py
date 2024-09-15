from questao_1_funcoes import validar_email

# Lista contendo as cadeias para teste da expressão regular da máscara de validação de email
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
    "a@b.com.br",                       # Válida
    "divulga@ufpa.br",                  # Válida
    "@",                                # Inválida (somente @)
    "@empresa.com.br",                  # Inválida (Não tem letras antes do @)
    "joao@.com.br",                     # Inválida (Não tem letras entre o @ e a terminação)
    "JOAO@empresa.com.br",              # Inválida (Tem letras maiúsculas)
    "joao@empresa.com.com.br",          # Inválida (Tem terminação inválida)
    "joao@empresa.org.br",              # Inválida (Tem terminação inválida)
    "joao@empresa.com.br123",           # Inválida (Tem terminação inválida)
    "joao@empresa",                     # Inválida (Tem terminação inválida)
    "joao@empresa.c",                   # Inválida (Tem terminação inválida)
    "joao@empresa.br..",                # Inválida (Tem terminação inválida)
    "joao@br.com",                      # Inválida (Tem terminação inválida)
    "usuario@domaincombr",              # Inválida (Tem terminação inválida)
    "usuario@domain.com"                # Inválida (Tem terminação inválida)
    "abc.@empresa.com.br",              # Inválida (Tem caracteres fora do alfabeto)
    "joao@empresa@com.br",              # Inválida (Tem mais de um @)
    "joao@empresa..br",                 # Inválida (Tem dois pontos seguidos)
    "joaoempresa.com.br",               # Inválida (Não tem o @)
    "joaonumeros123@empresa.com.br",    # Inválida (Tem números)
    "joao@numeros123.com.br",           # Inválida (Tem números)
    "_joao@empresa.com.br",             # Inválida (Tem caracteres especiais)
    "joao@empresa_123.com.br",          # Inválida (Tem caracteres especiais e números)
]

# Laço para iterar sobre a lista de cadeias e mostrar quais são válidas ou não
for email in emails_teste:
    print(f'Email: {email.ljust(30)} - Válido: {validar_email(email)}')
print()
