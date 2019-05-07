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

    def format_date(self):
        return datetime.datetime.fromtimestamp(self.get_data()).strftime('%Y-%m-%d %H:%M:%S')


    def addItem(self, item):
        self.__itens.append(item)

    def calcularTotal(self):
        total = 0
        for item in itens:
            total = total + float(item.calcularTotal)

        return total
