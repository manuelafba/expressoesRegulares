import re 

def validarCPF(cpf):
    """
    Valida um número de CPF de acordo com o formato padrão xxx.xxx.xxx-xx:

    Args: 
        cpf (string): número de CPF que será validado

    Returns:
        bool: Retorna True se o CPF for válido conforme os formatos especificados, caso contrário, retorna False.
    """
    regex = re.compile(r'^[0-9]{3}\.[0-9]{3}\.[0-9]{3}(\-[0-9]{2})$')
    if regex.fullmatch(cpf):
        return True
    else:
        return False