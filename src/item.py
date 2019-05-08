

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

    def getProduto(self):
        return self.__produto

    def calcularTotal(self):
        return float(self.getProduto().calcularPreco() * self.getQuantidade())

    def exibir_produto_como_linha(self):
        self.getProduto().exibirDadosProdutoAsLinha(self.getQuantidade())


#AREA DE TESTES
#a = item(11, "biscoito", 12, 1, 3)

#print(a.calcularTotal())
