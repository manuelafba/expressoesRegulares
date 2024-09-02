import re

def validarNome(nome):
    """
    Valida uma string como nome. Deve conter apenas letras maiúsculas e minúsculas, 
    deve ter no mínimo o primeiro e último nome (nome do meio é opcional). 
    Cada nome deve começar com uma letra maiúscula.

    Args: 
        nome (string): Nome que será validado.

    Returns:
        bool: Retorna True se o nome for válido conforme os formatos especificados, caso contrário, retorna False.
    """
    padrao_nome = re.compile(r'^[A-Z][a-z]*( [A-Z][a-z]*)* [A-Z][a-z]*$')
    return bool(padrao_nome.fullmatch(nome))

def validarEmail(email):
    """
    Valida uma string como email. Deve conter apenas letras minúsculas, 
    obrigatoriamente um '@' (e apenas um), com pelo menos uma letra minúscula antes e depois do '@', 
    e terminar com '.com.br' ou '.br'.

    Args: 
        email (string): Email que será validado.

    Returns:
        bool: Retorna True se o email for válido conforme os formatos especificados, caso contrário, retorna False.
    """
    padrao_email = re.compile(r'^[a-z]+@[a-z]+(\.com\.br|\.br)$')
    return bool(padrao_email.fullmatch(email))

def validarSenha(senha):
    """
    Valida uma string como senha. Deve conter ao menos uma letra maiúscula e uma minúscula, 
    pode conter números, mas não símbolos, e deve ter exatamente 8 caracteres.

    Args: 
        senha (string): Senha que será validada.

    Returns:
        bool: Retorna True se a senha for válida conforme os formatos especificados, caso contrário, retorna False.
    """
    padrao_senha = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])[a-zA-Z0-9]{8}$')
    return bool(padrao_senha.fullmatch(senha))

def validarCPF(cpf):
    """
    Valida um número de CPF de acordo com o formato padrão xxx.xxx.xxx-xx.

    Args: 
        cpf (string): Número de CPF que será validado.

    Returns:
        bool: Retorna True se o CPF for válido conforme os formatos especificados, caso contrário, retorna False.
    """
    padrao_cpf = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
    return bool(padrao_cpf.fullmatch(cpf))

def validarTelefone(telefone):
    """
    Valida números de telefone de acordo com os seguintes formatos:
    
    1. (xx) 9xxxx-xxxx
    2. (xx) 9xxxxxxxx
    3. xx 9xxxxxxxx 

    Args: 
        telefone (string): Número de telefone que será validado.

    Returns:
        bool: Retorna True se o número de telefone for válido conforme os formatos especificados, caso contrário, retorna False.
    """
    padrao_telefone = re.compile(r'^\(\d{2}\)\s9\d{4}-\d{4}$|^\(\d{2}\)\s9\d{8}$|^\d{2}\s9\d{8}$')
    return bool(padrao_telefone.fullmatch(telefone))

def validarData(data):
    """
    Valida datas de acordo com o formato dd/mm/aaaa hh:mm:ss, onde d, m, a, h, m, s são números.

    Args: 
        data (string): Data que será validada.

    Returns:
        bool: Retorna True se a data for válida conforme os formatos especificados, caso contrário, retorna False.
    """
    padrao_data_hora = re.compile(r'^\d{2}/\d{2}/\d{4}\s\d{2}:\d{2}:\d{2}$')
    return bool(padrao_data_hora.fullmatch(data))

def validarReal(real):
    """
    Valida números reais seguindo os seguintes critérios:
    
    1. Começa com um dos símbolos {+, -, ε}.
    2. Deve conter pelo menos um número.
    3. Deve ter exatamente um símbolo separador '.'.
    4. Finaliza com pelo menos um número.
    5. Exceção: números sem a parte fracionária também são aceitos.

    Args: 
        real (string): Número real que será validado.

    Returns:
        bool: Retorna True se o número real for válido conforme os formatos especificados, caso contrário, retorna False.
    """
    padrao_num_real = re.compile(r'^[+-]?\d+(\.\d+)?$')
    return bool(padrao_num_real.fullmatch(real))