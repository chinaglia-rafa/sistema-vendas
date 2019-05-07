

class item:
    def __init__(self, produto, quantidade, num):
        self.__produto = produto #VARIAVEL QUE GUARDA UM OBJETO DO TIPO PRODUTO
        self.__num = num
        self.__quantidade = quantidade

    #SETTERS
    def setNum(self, num):
        self.__num = num

    def setQuantidade(self, quantidade):
        self.__quantidade = quantidade

    #GETTERS
    def getNum(self):
        return self.__num

    def getQuantidade(self):
        return self.__quantidade


    #CALCULAR TOTAL
    def calcularTotal(self):
        total = float(self.getValor()*self.getQuantidade())
        return total


#AREA DE TESTES
#a = item(11, "biscoito", 12, 1, 3)

#print(a.calcularTotal())
