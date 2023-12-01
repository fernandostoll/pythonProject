l1 = int(input('digite o lado 1:'))
l2 = int(input('digite o lado 2:'))
l3 = int(input('digite o lado 3:'))

# Equilatero, isoceles, escaleno, não triangulo

if l1 > l2+l3 or l2 > l1+l3 or l3 > l1+l2:
    print('não triangulo')
elif l1 == l2 == l3:
    print('equilatero')
elif l1 == l2 or l2 == l3 or l1 == l3:
    print('isoceles')
else:
    print('escaleno')
