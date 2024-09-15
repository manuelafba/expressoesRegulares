from questao_1_funcoes import validar_nome

# Lista contendo as cadeias para teste da expressão regular da máscara de validação de nome
nomes_teste = [
    "Ada Lovelace",         # Válido
    "Alan Turing",          # Válido
    "Stephen Cole Kleene",  # Válido
    "Joao Silva",           # Válido
    "Ana Clara Souza",      # Válido
    "Lucas Oliveira Lima",  # Válido
    "Rafael Almeida",       # Válido
    "Bianca Almeida Souza", # Válido
    "Caio Moura",           # Válido
    "Larissa Souza",        # Válido
    "Roberto Carlo Bentes", # Válido
    "Gusta Henrique Souza", # Válido
    "Pedro H Silva",        # Válido
    "Roberto S",            # Válido
    "G C Silva",            # Válido
    "Alan",                 # Inválido (falta o sobrenome)
    "A1an",                 # Inválido (contém número)
    "Alan turing",          # Inválido (inicial minúscula do sobrenome)
    "alan Turing",          # Inválido (inicial minúscula do primeiro nome)
    "AlanTuring",           # Inválido (faltando espaço entre nome e sobrenome)
    "A1an Turing",          # Inválido (contém número)
    "Mariana  Silva",       # Inválido (espaço extra entre nome e sobrenome)
    "luis Mota",            # Inválido (inicial minúscula do primeiro nome) 
    "ana Maria",            # Inválido (inicial minúscula do primeiro nome)
    "Ana",                  # Inválido (apenas um nome)
    "Henrique da Silva",    # Inválido (nome do meio não começa com maiúscula)
    "Camila",               # Inválido (apenas um nome)
    "Joao da Silva",        # Inválido (nome do meio não começa com maiúscula)
    "Leonardo",             # Inválido (apenas um nome)    
    ]

# Laço para iterar sobre a lista de cadeias e mostrar quais são válidas ou não
for nome in nomes_teste:
    print(f'Nome: {nome.ljust(20)} - Válido: {validar_nome(nome)}')
print()
