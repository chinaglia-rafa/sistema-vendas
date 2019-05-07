from abc import ABC, abstractmethod #IMPORTANDO Modulo de Classes Abstratas

#CLASSE ABSTRATA PRODUTO
class produto(ABC):
    def __init__(self, codigo, descricao, valor):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valor = valor

    #SETTERS

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def setDescricao(self, descricao):
        self.__descricao = descricao

    def setValor(self, valor):
        self.__valor = valor

    #GETTERS

    def getCodigo (self):
        return self.__codigo

    def getDescricao (self):
        return self.__descricao

    def getValor (self):
        return self.__valor

    #Calculo Preço
    #METODO ABSTRATO
    @abstractmethod
    def calcularPreco(self):
        pass

    @abstractmethod
    def exibirDadosProduto(self):
        pass


class produtoNacional(produto):          #PRODUTO NACIONAL TEM UM IMPOSTO DE 10%
    def __init__(self, codigo, descricao, valor):
        super().__init__(codigo, descricao, valor)
        self.__imposto = 10  #IMPOSTO 10%

    #GETTERS
    def getImposto(self):
        return self.__imposto

    #SETTERS - NESSE CONTEXTO, NAO CABE SETAR UM VALOR PARA IMPOSTO, JA QUE TEMOS VALORES FIXOS
    #def setImposto(self, imposto):
        #self.__imposto = imposto

    def calcularPreco(self):
        preco = int(self.getValor()) + (int(self.getValor())*int(self.__imposto))/100
        return preco

    def exibirDadosProduto(self):
        print("Codigo do Produto: ", self.getCodigo())
        print("Descricao do Produto: ", self.getDescricao())
        print("Valor do Produto: ", self.calcularPreco(), "Reais")
        print("Imposto sobre o Produto: ", self.__imposto, "%")

class produtoImportado (produto):         #ALEM DO IMPOSTO, PRODUTO IMPORTADO, TEM UMA TAXA DE IMPORTAÇÃO DE 5%
    def __init__(self, codigo, descricao, valor):
        super().__init__(codigo, descricao, valor)
        self.__imposto = 10  #IMPOSTO 10%
        self.__taxa = 5 #TAXA 5%


    #GETTERS
    def getImposto (self):
        return self.__imposto

    def getTaxa (self):
        return self.__taxa

    #SETTERS'
    # def setImposto (self, imposto):
    #     self.__imposto = imposto
    #
    # def setTaxa (self, taxa):
    #     self.__taxa = taxa


    def calcularPreco(self):
        preco = int(self.getValor()) + (int(self.getValor())*int(self.__imposto))/100 + (int(self.getValor())*int(self.__taxa))/100
        return preco

    def exibirDadosProduto(self):
        print("Codigo do Produto: ", self.getCodigo())
        print("Descricao do Produto: ", self.getDescricao())
        print("Valor do Produto: ", self.calcularPreco(), "Reais")
        print("Imposto do Produto: ", self.getImposto(), "%")
        print("Taxa do Produto: ", self.getTaxa(), "%")





#Area de Testes

#produto1 = produtoNacional(5, 'Biscoito', 100)

#produto1.exibirDadosProduto()
