from produtos import produto

#Fazendo a classe item como filha de produto, para reaproveitar Codigo
#porem, como temos metodos abstratos, eles acabaram tendo que ser escritos
#e ficaram obsoletos na classe item

class item(produto):
    def __init__(self, codigo, descricao, valor, quantidade, num):
        super().__init__(codigo, descricao, valor)
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

    #METODOS ABSTRATOS
    def calcularPreco(self):
        pass

    def exibirDadosProduto(self):
        pass

    #CALCULAR TOTAL
    def calcularTotal(self):
        total = float(self.getValor()*self.getQuantidade())
        return total


#AREA DE TESTES
#a = item(11, "biscoito", 12, 1, 3)

#print(a.calcularTotal())
