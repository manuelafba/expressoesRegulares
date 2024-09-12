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
    regex = re.compile(f"^(MH|HM)({minimo_2m}|{minimo_1h}|{minimo_2h_1m})$")
    return bool(regex.fullmatch(familia))


def arranjo_letra_b(familia):
    """
    Expressão regular que representa arranjos familiares que tem casais heterossexuais mais
    velhos que os filhos e com uma quantidade ímpar de filhas mulheres.
    """
    regex = re.compile(r"^(MH|HM)h*mh*(h*mh*mh*)*$")
    return bool(regex.fullmatch(familia))


def arranjo_letra_c(familia):
    """
    Expressão regular que representa arranjos familiares que tem casais heterossexuais mais
    velhos que os filhos, com a filha mais velha mulher e o filho mais novo homem.
    """
    regex = re.compile(r"^(MH|HM)(m(m|h)*h)*$")
    return bool(regex.fullmatch(familia))


def arranjo_letra_d(familia):
    """
    Expressão regular que representa arranjos familiares que tem casais homossexuais mais velhos que
    os filhos, com pelo menos seis filhos, em que os dois primeiros filhos formam um casal e os
    últimos também.
    """
    regex = re.compile(r"^(MM|HH)(mh|hm)(m|h)(m|h)+(mh|hm)$")
    return bool(regex.fullmatch(familia))


def arranjo_letra_e(familia):
    """
    Expressão regular que representa arranjos familiares que tem casais homossexuais mais velhos
    que os filhos, em que o sexo dos filhos é alternado conforme a ordem de nascimento.
    """
    regex = re.compile(r"^(MM|HH)((mh)*|(hm)*|m(hm)*|h(mh)*)$")
    return bool(regex.fullmatch(familia))


def arranjo_letra_f(familia):
    """
    Expressão regular que representa arranjos familiares que tem casais homossexuais mais velhos
    que os filhos, com qualquer quantidade de filhos homens e mulheres, mas que não tiveram dois
    filhos homens consecutivos.
    """
    regex = re.compile(r'^(HH|MM)(m|h(?!h))*$')
    return bool(regex.fullmatch(familia))


def arranjo_letra_g(familia, x, y):
    """
    Expressão regular que representa arranjos familiares que tem no mínimo x ∈ ℕ e no máximo y ∈ ℕ,
    com x > 0, y > 0, e x ≤ y, de adultos (Hs ou Ms) mais velhos que os filhos, com qualquer
    quantidade de filhos homens e mulheres, mas que os três filhos mais novos não foram homens.
    """
    if x <= 0 or y <= 0 or x > y:
        return False
    regex = re.compile(r"^(M|H){" + str(x) + r"," + str(y) + r"}(h|hh|((m|h)*(m|mh|mhh)))?$")
    return bool(regex.fullmatch(familia))
