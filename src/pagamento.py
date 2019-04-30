from abc import ABC, abstractmethod #IMPORTANDO Modulo de Classes Abstratas

class pagamento(ABC):
    def __init__(self, tipoPagamento):
        self.__tipoPagamento = tipoPagamento


    #GETTERS
    def getTipoPagamento(self):
        return self.__tipoPagamento


    #SETTERS
    def setTipoPagamento(self, tipoPagamento):
        self.__tipoPagamento = tipoPagamento


    @abstractmethod
    def exibirDados (self):
        pass


class dinheiro(pagamento):
    def __init__(self, tipoPagamento):
        super().__init__(tipoPagamento)


    def exibirDados(self):
        print("Tipo de pagamento: ", self.getTipoPagamento())







class cheque (pagamento):
    def __init__(self, tipoPagamento, nomeEmissor, numeroCheque):
        super().__init__(tipoPagamento)
        self.__nomeEmissor = nomeEmissor
        self.__numeroCheque = numeroCheque

    #GETTERS
    def getNomeEmissor(self):
        return self.__nomeEmissor

    def getNumeroCheque(self):
        return self.__numeroCheque

    #SETTERS
    def setNomeEmissor(self, nomeEmissor):
        self.__nomeEmissor = nomeEmissor

    def setNumeroCheque(self, numeroCheque):
        self.__numeroCheque = numeroCheque


    def exibirDados (self):
        print("Tipo de Pagamento: ", self.getTipoPagamento())
        print("Nome do Emissor: ", self.getNomeEmissor())
        print("Numero Cheque: ", self.getNumeroCheque())



class cartao (pagamento):
    def __init__(self, tipoPagamento, nome, numero):
        super().__init__(tipoPagamento)
        self.__nome = nome
        self.__numero = numero

    #GETTERS
    def getNome(self):
        return self.__nome

    def getNumero(self):
        return self.__numero

    #SETTERS
    def setNome(self, nome):
        self.__nome = nome

    def setNumero(self, numero):
        self.__numero = numero


    def exibirDados (self):
        print("Tipo de Pagamento: ", self.getTipoPagamento())
        print("Nome do Portador: ", self.getNome())
        print("Numero do Cartao: ", self.getNumero())



#Area de testes

#pagamento1 = pagamento("teste")

#pagamento1.exibirDados()
