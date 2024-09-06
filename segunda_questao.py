import re

def arranjo_letra_a(familia):
    """
    Expressão regular que representa arranjos familiares que tem casais heterossexuais mais
    velhos que os filhos com pelo menos duas filhas mulheres, ou pelo menos um filho homem,
    ou ainda pelo menos dois filhos homens e uma filha mulher.
    """
    minimo_2m = r"((h|m)*m(h|m)*m(h|m)*)" 
    minimo_1h = r"((h|m)*h(h|m)*)"
    minimo_2h_1m = r"(((h|m)*h(h|m)*h(h|m)*m(h|m)*)|((h|m)*h(h|m)*m(h|m)*h(h|m)*)|((h|m)*m(h|m)*h(h|m)*h(h|m)*))"
    regex = re.compile(f"(MH|HM)({minimo_2m}|{minimo_1h}|{minimo_2h_1m})")
    return regex.fullmatch(familia)


def arranjo_letra_b(familia):
    """
    Expressão regular que representa arranjos familiares que tem casais heterossexuais mais
    velhos que os filhos e com uma quantidade ímpar de filhas mulheres.
    """
    regex = re.compile(r"(MH|HM)h*mh*(h*mh*mh*)*")
    return regex.fullmatch(familia)


def arranjo_letra_c(familia):
    """
    Expressão regular que representa arranjos familiares que tem casais heterossexuais mais
    velhos que os filhos, com a filha mais velha mulher e o filho mais novo homem.
    """
    regex = re.compile(r"(MH|HM)(m(m|h)*h)*")
    return regex.fullmatch(familia)


def arranjo_letra_d(familia):
    """
    Expressão regular que representa arranjos familiares que tem casais homossexuais mais velhos que
    os filhos, com pelo menos seis filhos, em que os dois primeiros filhos formam um casal e os
    últimos também.
    """
    regex = re.compile(r"(MM|HH)(mh|hm)(m|h){2,}(mh|hm)")
    return regex.fullmatch(familia)


def arranjo_letra_e(familia):
    """
    Expressão regular que representa arranjos familiares que tem casais homossexuais mais velhos
    que os filhos, em que o sexo dos filhos é alternado conforme a ordem de nascimento.
    """
    regex = re.compile(r"(MM|HH)((mh)*|(hm)*|m(hm)*|h(mh)*)")
    return regex.fullmatch(familia)


def arranjo_letra_f(familia):
    """
    Expressão regular que representa arranjos familiares que tem casais homossexuais mais velhos
    que os filhos, com qualquer quantidade de filhos homens e mulheres, mas que não tiveram dois
    filhos homens consecutivos.
    """
    regex = re.compile(r'^(HH|MM)(m|h(?!h))*$')
    return regex.fullmatch(familia)


def arranjo_letra_g(familia):
    """
    Expressão regular que representa arranjos familiares que tem no mínimo x ∈ ℕ e no máximo y ∈ ℕ,
    com x > 0, y > 0, e x ≤ y, de adultos (Hs ou Ms) mais velhos que os filhos, com qualquer
    quantidade de filhos homens e mulheres, mas que os três filhos mais novos não foram homens.
    """
    # Loop para solicitar ao usuário os valores de X e Y
    while True:
        # O valor de X é solicitado até o usuário digitar um valor válido, ou seja, maior que zero.
        x = int(input("Valor de X: "))
        if x > 0:
            break
        print("Valor inválido para X. Digite um valor >= 0.")
    while True:
        # O valor de Y só é solicitado quando o usuário digitar um valor válido para X
        # # O valor de Y é solicitado até o usuário digitar um valor válido, ou seja, maior que zero e maior ou igual a X.
        y = int(input("Valor de Y: "))
        if y > 0 and x <= y:
        # Saída do loop caso X e Y tenham valores válidos
            break
        print("Valor inválido para Y. Digite um valor >= 0 e >= X.")
    regex = re.compile(r"^(M|H){" + str(x) + r"," + str(y) + r"}(m|mm|mmm|(m|h)*mmm+)?")
    return regex.fullmatch(familia)

# TESTES
if arranjo_letra_g("MHmhmmmh"):
    print("Aceita")
else:
    print("Rejeita")
