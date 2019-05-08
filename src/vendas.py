import time
import datetime

class venda:
    """Classe responsável por gerenciar e armazenar as vendas cadastradas"""
    def __init__(self, numero, tipo_pagamento, cliente):
        self.__numero = numero
        self.__tipo_pagamento = tipo_pagamento
        self.__cliente = cliente
        self.__data = time.time()
        self.__itens = []

    def get_numero(self):
        return self.__numero

    def get_tipo_pagamento(self):
        return self.__tipo_pagamento

    def get_cliente(self):
        return self.__cliente

    def get_data(self):
        return self.__data

    def get_itens(self):
        return self.__itens

    def format_date(self):
        return datetime.datetime.fromtimestamp(self.get_data()).strftime('%d/%m/%Y %H:%M:%S')


    def addItem(self, item):
        self.__itens.append(item)

    def calcularTotal(self):
        total = 0
        for item in self.get_itens():
            total = total + float(item.calcularTotal())

        return total

    def exibir(self, show_products = False):
        print("Nota Fiscal #", self.get_numero())
        print("Data da compra:", self.format_date())
        if show_products:
            print("\nCod.".ljust(4), end = " ")
            print("Descrição".ljust(40), end = "  ")
            print("Valor".ljust(15), end = " ")
            print("Qtd".ljust(8), end = " ")
            print("Total".ljust(12), end = " ")
            print("Imposto / Taxa")
            for item in self.get_itens():
                item.exibir_produto_como_linha()
        print("\nTotal gasto pelo cliente: R$", "{:.2f}".format(self.calcularTotal()))
        self.get_tipo_pagamento().exibirDados()
