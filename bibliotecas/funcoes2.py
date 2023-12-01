def iscpf(cpf):
    import re
    cpf_novo = re.sub(r'\D', '', cpf)

    digitos = []
    for i in cpf_novo:
        digitos.append(int(i))

    #TODO limpar os dados do cpf, e deixar em lista digitos

    total = 0
    mult = 10
    for digito in digitos[:-2]:
        total += digito * mult
        mult -= 1
    digito_ver1 = 11 - total % 11
    if digito_ver1 >= 10:
        digito_ver1 = 0

    total = 0
    mult = 11
    for digito in digitos[:-1]:
        total += digito * mult
        mult -= 1
    digito_ver2 = 11 - total % 11
    if digito_ver2 >= 10:
        digito_ver2 = 0


    if digito_ver1 == digitos[9] and digito_ver2 == digitos[10]:
        return True
    return False

print(iscpf('111.990.979-18'))