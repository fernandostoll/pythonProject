class veiculo:
    def __init__(self, propietario, ano, modelo, marca, cor, adometro, ligado=False):
        self.propietario = propietario
        self.ano = ano
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.odometro = odometro
        self.ligado = ligado

    def show_owner(self):
        return self.propietario

    def show_info(self):
        return f'{self.marca}, {self.modelo}, {self.ano}'

    def new_painting(self, color):
        self.cor = color

    def start_engine(self):

    def stop_engine(self):

    def run(self, miles):
        if self.ligado:
            self.odometro += miles