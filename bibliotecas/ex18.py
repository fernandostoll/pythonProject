def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32

def dias_ano(ano):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        return 366
    return 365