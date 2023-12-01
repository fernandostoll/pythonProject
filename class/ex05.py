class bomba_de_de_combustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor_abastecido):
        litros_abastecidos = valor_abastecido / self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            return f"Foram abastecidos {litros_abastecidos:.2f} litros de {self.tipo_combustivel}."
        else:
            return "Quantidade de combustível insuficiente na bomba."

    def abastecer_por_litro(self, litros_abastecidos):
        valor_a_pagar = litros_abastecidos * self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            return f"Valor a pagar: R$ {valor_a_pagar:.2f}"
        else:
            return "Quantidade de combustível insuficiente na bomba."

    def alterar_valor(self, novo_valor_litro):
        self.valor_litro = novo_valor_litro

    def alterar_combustivel(self, novo_tipo_combustivel):
        self.tipo_combustivel = novo_tipo_combustivel

    def alterar_quantidade_combustivel(self, nova_quantidade_combustivel):
        self.quantidade_combustivel = nova_quantidade_combustivel

    def exibir_informacoes(self):
        return f"Tipo de Combustível: {self.tipo_combustivel}\nValor por Litro: R$ {self.valor_litro:.2f}\nQuantidade de Combustível: {self.quantidade_combustivel:.2f} litros"

    # Exemplo de uso da classe BombaCombustivel
    bomba = bomba_de_combustivel("Gasolina", 5.0, 1000.0)

    print(bomba.abastecer_por_valor(50.0))  # Abastece R$ 50
    print(bomba.abastecer_por_litro(10.0))  # Abastece 10 litros
    print(bomba.exibir_informacoes())

    bomba.alterar_valor(4.5)  # Altera o valor por litro
    bomba.alterar_quantidade_combustivel(900.0)  # Altera a quantidade de combustível

    print(bomba.exibir_informacoes())

