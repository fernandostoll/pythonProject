class retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudar_lados(self, novo_ladoA, novo_ladoB):
        self.ladoA = novo_ladoA
        self.ladoB = novo_ladoB

    def retornar_lados(self):
        return self.ladoA, self.ladoB

    def calcular_area(self):
        return self.ladoA * self.ladoB

    def calcular_perimetro(self):
        return 2 * (self.ladoA + self.ladoB)

ladoA = float(input('informe o comprimento do local em metros: '))
ladoB = float(input('informe a largura do local em metros: '))
parede = retangulo(ladoA, ladoB)

comprimento_piso = float(input('informe o comprimentode um piso em metros: '))
piso = retangulo(comprimento_piso, area_piso)

area_parede = parede.calcular_area()
area_piso = piso.calcular_area()

quantidade_pisos = area_parede / area_piso

print(f"A área da parede é {area_parede} metros quadrados.")
print(f"A área de um piso é {area_piso} metros quadrados.")
print(f"Você precisará de {quantidade_pisos} pisos para cobrir a parede.")