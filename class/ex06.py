class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def ver_bucho(self):
        return f"Conteúdo do estômago de {self.nome}: {', '.join(self.bucho)}"

    def digerir(self):
        if len(self.bucho) > 0:
            print(f"{self.nome} está digerindo {self.bucho.pop(0)}")
        else:
            print(f"{self.nome} não tem nada no estômago para digerir.")

    # Criando dois macacos
    macaco1 = Macaco("Macaco1")
    macaco2 = Macaco("Macaco2")

    # Alimentando os macacos com 3 alimentos diferentes
    macaco1.comer("Banana")
    macaco2.comer("Maçã")
    macaco1.comer("Mamão")

    # Verificando o conteúdo do estômago dos macacos após cada refeição
    print(macaco1.ver_bucho())
    print(macaco2.ver_bucho())

    # Fazendo os macacos digerirem
    macaco1.digerir()
    macaco2.digerir()

    # Verificando o conteúdo do estômago após a digestão
    print(macaco1.ver_bucho())
    print(macaco2.ver_bucho())