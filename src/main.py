import platform
import os
from cliente import *
from item import *
from pagamento import *
from produtos import *


#DEFINIÇÃO DE LISTAS DE ARMAZENAMENTO
clientes = []
produtos = []


print(platform.system())
def clear_screen():
    if platform.system() == 'Linux' or platform.system() == 'Darwin':  #Rafa bobao nao sabe escrever Darwin
        os.system('clear')
    else:
        os.system('cls')


def main_menu():
    """ Mostra o menu principal na tela e retorna a escolha """

    clear_screen()

    print("Sistema de Vendas <INSIRA_NOME_AQUI> 0.1 beta.\n")
    menu_options = ['Cadastrar', 'Registrar Compra', 'Relatórios', 'Salvar Dados', 'Carregar Dados', 'Sair']
    i = 1
    for menu_item in menu_options:
        print(("[ " + str(i) + " ]"), menu_item)
        i += 1
    option = -1
    try:
        option = int(input("Escolha uma opção: "))
    except Exception as err:
        print("Use apenas números entre 1 e 6.")
        input()
        return main_menu()

    if 0 < option < 7:
        return option
    else:
        return main_menu()


def menu_cadastrar():
    """ Mostra o submenu de cadastro e retorna a opção """

    clear_screen()

    print("Sistema de Vendas <INSIRA_NOME_AQUI> 0.1 beta.\n")
    print("[ 1 ] Cadastrar")
    menu_options = ['Cliente', 'Produto', 'Voltar']
    i = 1
    for menu_item in menu_options:
        print(("   [ " + str(i) + " ]"), menu_item)
        i += 1
    option = -1
    try:
        option = int(input("Escolha uma opção: "))
    except Exception as err:
        print("Use apenas números entre 1 e", str(len(menu_options)))
        input()
        return menu_cadastrar()

    if 0 < option <= len(menu_options):
        return option
    else:
        return menu_cadastrar()


def menu_relatorios():
    """ Mostra o submenu de relatórios e retorna a opção """

    clear_screen()

    print("Sistema de Vendas <INSIRA_NOME_AQUI> 0.1 beta.\n")
    print("[ 3 ] Relatórios")
    menu_options = ['Lista de Clientes', 'Buscar Cliente', 'Gastos de um cliente',
    'Lista de Produtos', 'Buscar Produto', 'Vendas', 'Buscar Venda',
    'Vendas por tipo de pagamento (simplificada)',
    'Vendas por tipo de pagamento (etalhada)', 'Voltar']
    i = 1
    for menu_item in menu_options:
        print(("   [ " + str(i) + " ]"), menu_item)
        i += 1
    option = -1
    try:
        option = int(input("Escolha uma opção: "))
    except Exception as err:
        print("Use apenas números entre 1 e", str(len(menu_options)))
        input()
        return menu_relatorios()

    if 0 < option <= len(menu_options):
        return option
    else:
        return menu_relatorios()


opt = -1
sub_opt = -1;

while opt == -1:
    opt = main_menu()
    if opt == 1:
        #  Abrindo submenu de cadastro
        sub_opt = -1;
        while sub_opt == -1:
            sub_opt = menu_cadastrar()
            if sub_opt == 1: #   Cadastro de Cliente
                """ CADASTRANDO CLIENTE - @author: Marcelo Eduardo - @email: marceloer2011@gmail.com """

                nome = input("Digite o nome do cliente a ser cadastrado: ")
                cpf = input("Digite o CPF do cliente: ")
                clientes.append(cliente(cpf, nome))
                sub_opt = -1

            elif sub_opt == 2: #   Cadastro de Produto
                """ CADASTRANDO PRODUTO - @author: Marcelo Eduardo - @email: marceloer2011@gmail.com """

                codigo = input("Informe o codigo do produto: ")
                descricao = input("Digite a descrição do produto: ")
                valor = input("Informe o valor do produto: ")
                tipo = input("Qual o tipo do produto? (Nacional, Importado): ")

                while(str.lower(tipo) != "nacional" and str.lower(tipo) != "importado"): #REPETE ATE O TIPO DE PRODUTO SER VALIDO
                    if(str.lower(tipo) == "nacional"):  #convertendo a string para minusculo antes de comparar
                        produtos.append(produtoNacional(codigo, descricao, valor)) #caso for nacional, cria um objeto do tipo Nacional e coloca na lista(array)
                    elif(str.lower(tipo) == "importado"):  #convertendo a string para minusculo antes de comparar
                        produtos.append(produtoImportado(codigo, descricao, valor)) #caso for importado, cria um objeto do tipo Importado e coloca na lista(array)
                    else:
                        print("Tipo de produto invalido, tente uma das opções disponíveis!")
                        tipo = input("Qual o tipo do produto? (Nacional, Importado): ")
                    sub_opt = -1

            elif sub_opt == 3:
                #   Voltando para o menu principal
                opt = -1
                print("voltando do submenu para o menu principal")

    elif opt == 2:
        #   Registrar Compra
        pass
    elif opt == 3:
        sub_opt = -1;
        while sub_opt == -1:
            sub_opt = menu_relatorios()
            if sub_opt == 1:
                #   Lista de Clientes
                """ Listar todos os clientes - @author: Marcelo Eduardo - @email: marceloer2011@gmail.com """
                for cliente in clientes:   #Para cada item no array que guarda os clientes, utilize a função de exibir os dados do cliente
                    cliente.exibirCliente()
            elif sub_opt == 2:
                #   Buscar Cliente  AINDA É NECESSARIO TRATAR O CASO EM QUE O USUARIO ENTRA ALGO INVALIDO (NEM CPF NEM NOME)
                busca = input("Deseja buscar o cliente por CPF ou Nome? ")

                if(str.lower(busca) == "cpf"):
                    cpf = input("Digite o CPF que deseja buscar: ")
                    for cliente in clientes:
                        if(cliente.getCPF() == cpf):
                            cliente.exibirCliente()
                elif(str.lower(busca) == "nome"):
                    nome = input("Digite o Nome que deseja buscar: ")
                    for cliente in clientes:
                        if(cliente.getNome() == nome):
                            cliente.exibirCliente()
            elif sub_opt == 3:
                #   Gastos de um cliente
                pass
            elif sub_opt == 4:
                #   Produto Geral
                pass
            elif sub_opt == 5:
                #   Buscar produto
                pass
            elif sub_opt == 6:
                #   Vendas Geral
                pass
            elif sub_opt == 7:
                #   Buscar Venda
                pass
            elif sub_opt == 8:
                #   Venda por tipo de pagamento (simples)
                pass
            elif sub_opt == 9:
                #   Venda por tipo de pagamento (detalhada)
                pass
            elif sub_opt == 10:
                #   Voltando para o menu principal
                opt = -1
                sub_opt = -1
                print("voltando do submenu para o menu principal")
    elif opt == 4:
        #   Salvar Dados
        pass
    elif opt == 5:
        #   Carregar Dados
        pass
    elif opt == 6:
        pass

print("EXECUTANDO OPÇÃO", opt, "COM SUBMENU", sub_opt)
