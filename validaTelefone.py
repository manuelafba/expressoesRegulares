import re

def validarTelefone(telefone):
    """
    Valida números de telefone de acordo com os seguintes formatos:
    
    1. (xx) 9xxxx-xxxx
    2. (xx) 9xxxxxxxx
    3. xx 9xxxxxxxx

    Exemplos de números aceitos:
    - "(91) 99999-9999"
    - "(91) 999999999"
    - "91 999999999"
    
    Exemplos de números rejeitados:
    - "(91) 59999-9999" 
    - "99 99999-9999"   
    - "(94) 95555-5555"  

    Args: 
        telefone (string): número de telefone que será validado

    Returns:
        bool: Retorna True se o número de telefone for válido conforme os formatos especificados, caso contrário, retorna False.
    """
    regex = re.compile(r'^\(\d{2}\)\s9{1}\d{4}\-\d{4}$ | ^\(?\d{2}\)?\s9{1}\d{8}$')
    if regex.fullmatch(telefone):
        return True
    else:
        return False
