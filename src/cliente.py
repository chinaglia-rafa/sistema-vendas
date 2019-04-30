from abc import ABC, abstractmethod


# Classe Abstrata em Python teste
# class abstract (ABC):
#     @abstractmethod
#     def seila (self):
#         pass
#
# class derivated (abstract):
#     def seila (self):
#         print ("Teste")

# Métodos a serem feitos:
#     -Clientes Geral: Exibir dados de todos os clientes cadastrados;
#
#     -Cliente Específico: Exibir dados de um determinado cliente;
#
#     -Gasto de um Cliente: Exibe o total gasto por um determinado cliente,
#     exibindo os detalhes gerais das compras, isto é, número de nota fiscal,
#     data da compra, total gasto com a compra, informação sobre o pagamento.
#     No fim o relatório deve exibir o total geral gasto pelo cliente;
#
#     -Produto Geral: Exibe dados dos Produtos
#
#     -Produto Especificos: Exibe dados de um determinado Produto
#
#     -Vendas Geral: Exibe dados de todas as vendas. Deve exibir nome do cliente,
#     CPF, número de nota fiscal, data da compra, total gasto, tipo de pagamento.
#     No fim deve exibir o total geral acumulado.
#
#     -Vendas Especifico: Exibição detalhada de uma venda específica, exibe todos os dados
#
#     -Vendas por tipo de pagamento - Versao simplificada: O usuario escolhe um
#     tipo de pagamento (dinheiro, cheque ou cartão) e são exibidos todos os detalhes de uma venda.
#
#     - Vendas por tipo de pagamento - Versao detalhada: O usuatrio escohle um tipo de
#     pagamento (dinheiro, cheque ou cartao) e são exibidos todos os detalhes de venda.

class cliente:
    def __init__ (self, cpf, nome):
        self.__cpf = cpf
        self.__nome = nome

    def getCPF (self):
        return self.__cpf

    def getNome (self):
        return self.__nome

    def setCPF (self):
        self.__cpf = cpf

    def setNome (self):
        self.__nome = nome

    def exibirCliente (self):
        print ("Nome: ", self.getNome())
        print ("CPF: ", self.getCPF())
