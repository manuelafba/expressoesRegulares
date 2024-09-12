from questao_1_funcoes import validar_nome

nomes_teste = [
        "Ada Lovelace",         # Válido
        "Alan Turing",          # Válido
        "Stephen Cole Kleene",  # Válido
        "Joao Silva",           # Válido
        "Maria Joaquina",       # Válido
        "Ana Clara Souza",      # Válido
        "Carla Correia",        # Válido
        "Lucas Oliveira Lima",  # Válido
        "Joao Pedro Souza",     # Válido
        "Rafael Almeida",       # Válido
        "Bianca Almeida Souza", # Válido
        "Alessandra Silva",     # Válido
        "Luana Costa",          # Válido
        "Gustavo Silva",        # Válido
        "Caio Moura",           # Válido
        "Lucas Pereira",        # Válido
        "Mateus Lira",          # Válido
        "Roberto Almeida",      # Válido
        "Paulo Souza",          # Válido
        "Fernanda Alves",       # Válido
        "Lucas Costa",          # Válido
        "Paulo Nogueira",       # Válido
        "Aline Ferreira",       # Válido
        "Andre Silva",          # Válido
        "Larissa Souza",        # Válido
        "Pedro Henrique Silva", # Válido
        "Ana Paula",            # Válido
        "Joao Lucas Pereira",   # Válido
        "Roberto Carlo Bentes", # Válido
        "Gusta Henrique Souza", # Válido
        "Pedro H Silva",        # Inválido (inicial abreviada no nome do meio) ????????????????????
        "Roberto S",            # Inválido (nome incompleto) ???????????????
        "Gabriel C Silva",      # Inválido (nome do meio abreviado) ????????????????????
        "Alan",                 # Inválido (somente um nome)
        "A1an",                 # Inválido (contém número)
        "Alan turing",          # Inválido (sobrenome começa com letra minúscula)
        "alan Turing",          # Inválido (nome começa com letra minúscula)
        "AlanTuring",           # Inválido (faltando espaço entre nome e sobrenome)
        "A1an Turing",          # Inválido (contém número)
        "Mariana  Silva",       # Inválido (espaço extra entre nome e sobrenome)
        "Carlos",               # Inválido (só um nome)
        "luis Mota",            # Inválido (primeiro nome minúsculo)
        "Joao",                 # Inválido (apenas um nome)    
        "ana Maria",            # Inválido (primeiro nome minúsculo)
        "Ana",                  # Inválido (apenas um nome)
        "Fernanda",             # Inválido (apenas um nome)
        "Ricardo",              # Inválido (apenas um nome)
        "Lucas de Oliveira",    # Inválido (contém preposição)
        "Henrique da Silva",    # Inválido (contém preposição)
        "Camila",               # Inválido (apenas um nome)
        "Joao da Silva",        # Inválido (contém preposição)
        "Leonardo",             # Inválido (apenas um nome)    
        "Flavia",               # Inválido (apenas um nome)
        "Renato",               # Inválido (apenas um nome)
        "Carla",                # Inválido (apenas um nome)
        "Antonio",              # Inválido (apenas um nome)
    ]

for nome in nomes_teste:
    print(f'Nome: {nome.ljust(20)} - Válido: {validar_nome(nome)}')
print()
