#abordagem recursiva:
def fatorial_recursivo(numero):
    if numero == 0:
        return 1
    else:
        return numero * fatorial_recursivo(numero - 1)

# Exemplo de uso:
numero = 5
resultado = fatorial_recursivo(numero)
print(f"O fatorial de {numero} é igual a {resultado}")

#abordagem interativa
def fatorial_iterativo(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

# Exemplo de uso:
numero = 5
resultado = fatorial_iterativo(numero)
print(f"O fatorial de {numero} é igual a {resultado}")