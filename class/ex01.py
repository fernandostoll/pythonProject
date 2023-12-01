class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circuferencia = circunferencia
        self.material = material

    def trocar_cor(self, nova_cor):
        self.cor = nova_cor
    def mostra_cor(self):
        return self.cor

# Criando uma instância de Bola
minha_bola = Bola("vermelha", 30, "plástico")

# Mostrando a cor atual
print("Cor atual:", minha_bola.mostrar_cor())

# Trocando a cor da bola
minha_bola.trocar_cor("azul")

# Mostrando a nova cor
print("Nova cor:", minha_bola.mostrar_cor())
