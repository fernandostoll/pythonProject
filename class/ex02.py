class quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mudar_lado(self, novo_lado):
        self.tamanho_lado = novo_lado

    def retornar_lado(self):
        return self.tamanho_lado

    def calcular_area(self):
        return self.tamanho_lado ** 2

    def calcular_perimetro(self):
        return 4 * self.tamanho_lado