import platform
import os
import pickle
from cliente import *
from item import *
from pagamento import *
from produtos import *
from vendas import *


#DEFINIÇÃO DE LISTAS DE ARMAZENAMENTO
clientes = []
produtos = []
vendas = []

def clear_screen():
    if platform.system() == 'Linux' or platform.system() == 'Darwin':
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
    'Vendas por tipo de pagamento (detalhada)', 'Voltar']
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

def buscar_cliente(lista_clientes):
    busca = "nada"

    while(str.lower(busca) != "cpf" and str.lower(busca) != "nome"):
        busca = input("Deseja buscar o cliente por CPF ou Nome? ")
        if(str.lower(busca) == "cpf"):
            cpf = input("Digite o CPF que deseja buscar: ")
            for cliente in lista_clientes:
                if(cliente.getCPF() == cpf):
                    return cliente
            return False
        elif(str.lower(busca) == "nome"):
            nome = input("Digite o Nome que deseja buscar: ")
            for cliente in lista_clientes:
                if(str.lower(cliente.getNome()) == str.lower(nome)):
                    return cliente
            return False
        else:
            print("Por favor, escolha uma das opções disponíveis!")

def buscarProduto(lista_produtos):
    busca = "nada"
    while(str.lower(busca) != "codigo" and str.lower(busca) != "descricao"):
        busca = input("Você deseja buscar o produto através do código ou da descrição? ")
        if(str.lower(busca) == "codigo"):
            codigo = input("Digite o código do produto: ")
            for produto in lista_produtos:
                if(produto.getCodigo() == codigo):
                    return produto

        elif(str.lower(busca) == "descricao"):
            descricao = input("Digite a descrição do produto: ")
            for produto in lista_produtos:
                if(str.lower(produto.getDescricao()) == str.lower(descricao)):
                    return produto
        else:
            print("Por favor, escolha uma das opções disponíveis!")

    return False

def buscar_venda(lista_vendas):
    codigo = input("Digite o código da venda: ")
    for venda in lista_vendas:
        if(venda.get_numero() == codigo):
            return venda
    return False

opt = -1
sub_opt = -1
# TESTES
# print("\n\nFIQUE ATENTO! DADOS DE TESTE ESTÃO SENDO USADOS A PARTIR DA LINHA 145!\n\n")
# rafa = cliente('400', 'Rafael Araújo Chinaglia')
# heitor = cliente('666', 'Heitor')
# clientes.append(rafa)
# clientes.append(heitor)
# p1 = produtoNacional('1', 'Dark Souls: Prepare to die Edition', 299)
# p2 = produtoImportado('1', 'Dark Souls III', 299)
# meuitem = item(p2, 2, 987)
# produtos.append(p1)
# produtos.append(p2)
# v = venda('123', dinheiro(), rafa)
# v.addItem(meuitem)
# meuitem = item(p1, 3, 789)
# v.addItem(meuitem)
# v.exibir(True)
# vendas.append(v)
#
# exit(0)

while opt == -1:
    opt = main_menu()
    if opt == 1:
        #  Abrindo submenu de cadastro
        sub_opt = -1
        while sub_opt == -1:
            sub_opt = menu_cadastrar()
            if sub_opt == 1: #   Cadastro de Cliente
                """ CADASTRANDO CLIENTE - @author: Marcelo Eduardo - @email: marceloer2011@gmail.com """
                flag = 0 #VARIAVEL PRA AUXILIAR NO CADASTRO
                nome = input("Digite o nome do cliente a ser cadastrado: ")
                cpf = input("Digite o CPF do cliente: ")
                opcao = "nada"
                for percorre_clientes in clientes:
                    if(percorre_clientes.getCPF() == cpf):
                        while(str.lower(opcao) !=  "sim" and str.lower(opcao) != "nao"):
                            opcao = input("Ja temos um cliente cadastrado com esse CPF, deseja prosseguir e fazer um novo cadastro com esses dados? (SIM ou NAO) ")
                            if(str.lower(opcao) == "sim"):
                                clientes.append(cliente(cpf, nome))
                                input("Cliente cadastrado, aperte ENTER para continuar")
                            elif(str.lower(opcao) == "nao"):
                                print("Cancelando cadastro...")
                                input("Aperte ENTER para continuar")
                            else:
                                print("Por favor escolha SIM ou NAO")
                            flag = 1
                if(flag == 0):
                    clientes.append(cliente(cpf, nome))
                    input("Cliente cadastrado, aperte ENTER para continuar")

                sub_opt = -1

            elif sub_opt == 2: #   Cadastro de Produto
                """ CADASTRANDO PRODUTO - @author: Marcelo Eduardo - @email: marceloer2011@gmail.com """

                codigo = input("Informe o codigo do produto: ")
                descricao = input("Digite a descrição do produto: ")
                valor = input("Informe o valor do produto: ")

                tipo = "nenhum"
                opcao = "nada"

                while(str.lower(tipo) != "nacional" and str.lower(tipo) != "importado"): #Loop de cadastro
                    tipo = input("Qual o tipo do produto? (Nacional, Importado): ")
                    if(str.lower(tipo) == "nacional"):  #convertendo a string para minusculo antes de comparar
                        produtos.append(produtoNacional(codigo, descricao, valor)) #caso for nacional, cria um objeto do tipo Nacional e coloca na lista(array)
                    elif(str.lower(tipo) == "importado"):  #convertendo a string para minusculo antes de comparar
                        produtos.append(produtoImportado(codigo, descricao, valor)) #caso for importado, cria um objeto do tipo Importado e coloca na lista(array)
                    else:
                        print("Tipo de produto invalido, tente uma das opções disponíveis!")
                sub_opt = -1


            elif sub_opt == 3:
                #   Voltando para o menu principal
                opt = -1
                print("voltando do submenu para o menu principal")

    elif opt == 2:
        #   Registrar Compra
        #   POSSIVELMENTE PRONTO
        aux = 0
        opcao = ""
        while(aux != 1 and opcao != "nao"):
            numero = input("Digite o numero da compra: ")
            #REGISTRANDO OS ITENS DA COMPRA
            aux_reset = 1
            opcao_venda = "nada"
            aux_itens = []
            numero_do_item = ""
            print("Iremos precisar realizar uma busca do(s) produto(s) a serem registrados na compra: ")
            while(str.lower(opcao_venda) != "nao" and str.lower(opcao) != "nao"):
                opcao = ""
                aux_produto = buscarProduto(produtos)
                if(aux_produto != False):
                    quantidade_produtos = input("Quantos produtos desse mesmo tipo foram comprados? ")
                    aux_num = input("Por favor, digite agora o número de registro do item: ")
                    aux_item = item(aux_produto, quantidade_produtos, aux_num)
                    aux_itens.append(aux_item)
                    opcao_venda = input("Registro de item feito com sucesso! Deseja registrar outro item? (SIM ou NAO): ")
                else:
                    while(str.lower(opcao) != "sim" and str.lower(opcao) != "nao"):
                        opcao = input("Para registrar uma compra é necessário que o produto esteja cadastrado, deseja tentar novamente? (SIM, NAO): ")
                        if(str.lower(opcao) != "sim" and str.lower(opcao) != "nao"):
                            input("Por favor, escolha uma das opções dadas! (Pressione ENTER para continuar...)")

                #AQUI VERIFICAMOS A RESPOSTA DO CLIENTE E GUARDAMOS, PARA VER SE CONTINUAMOS COM O MENU OU SIMPLESMENTE RESETAMOS ELE
                if(str.lower(opcao) == "nao"):
                    aux_reset = 0
                    aux = 1



            #BUSCAR CLIENTE
            aux_busca_cliente = 0
            if(aux_reset == 1):
                opcao = ""
                while(aux_busca_cliente == 0 and str.lower(opcao) != "nao"):
                    opcao = ""
                    print("Agora necessitamos dos dados do cliente que fez a compra, iremos buscar no banco de dados:")
                    aux_cliente = buscar_cliente(clientes)
                    if(aux_cliente != False):
                        print("Cliente encontrado!")
                        aux_busca_cliente = 1

                    else: #CLIENTE NAO ENCONTRADO
                        while(str.lower(opcao) != "sim" and str.lower(opcao) != "nao"):
                            opcao = input("Para registrar uma compra, é necessário que o cliente esteja cadastrado, deseja tentar novamente? (SIM, NAO): ")
                            if(str.lower(opcao) != "sim" and str.lower(opcao) != "nao"):
                                input("Por favor, escolha uma das opções dadas! (Pressione ENTER para continuar...)")

                    if(str.lower(opcao) == "nao"):
                        aux_reset = 0
                        aux = 1

            if(aux_reset == 1):
                tipo_pagamento = ""
                #Verifica o tipo de pagamento e pede os dados necessarios
                print("Registre por favor agora o método de pagamento e os dados necessarios")
                while(str.lower(tipo_pagamento) != "cheque" and str.lower(tipo_pagamento) != "cartao" and str.lower(tipo_pagamento) != "dinheiro"):
                    tipo_pagamento = ""
                    tipo_pagamento = input("ESCOLHA DO MÉTODO DE PAGAMENTO (Cartao, Dinheiro, Cheque): ")
                    if(str.lower(tipo_pagamento) == "dinheiro"):
                        payment = dinheiro()
                    elif(str.lower(tipo_pagamento) == "cartao"):
                        nome = input("Digite o nome do Titular do cartão: ")
                        num = input("Digite o numero do cartão: ")
                        payment = cartao(nome, num)
                    elif(str.lower(tipo_pagamento) == "cheque"):
                        nome = input("Digite o nome do Emissor do cheque: ")
                        num = input("Digite o numero do cheque: ")
                        payment = cheque(nome, num)
                    else:
                        input("Por favor, escolha uma das opções dadas! (Pressione ENTER para continuar...)")


            if(aux_reset == 1):
                aux_venda = venda(numero, payment, aux_cliente)
                for item in aux_itens:
                    aux_venda.addItem(item)
                vendas.append(aux_venda)
                input("Compra registrada com sucesso... (Pressione ENTER para continuar...)")
                aux = 1


        opt = -1


    elif opt == 3:
        #   Relatórios
        sub_opt = -1
        while sub_opt == -1:
            sub_opt = menu_relatorios()
            #SUB-OPÇÃO 1
            if sub_opt == 1:
                #   Lista de Clientes
                print("\nListando Clientes Cadastrados!")
                for cliente in clientes:   #Para cada item no array que guarda os clientes, utilize a função de exibir os dados do cliente
                    print("")
                    cliente.exibirCliente()
                input("Pressione ENTER para continuar...")
                sub_opt = -1

            #SUB-OPÇÃO 2
            elif sub_opt == 2:  # TODO: adicionar loop de tentar novamente
                #   Buscar Cliente
                cliente = buscar_cliente(clientes)
                if cliente != False:
                    print("")
                    cliente.exibirCliente()
                    input()
                else:
                    input("Cliente não encontrado!")

                sub_opt = -1
            #SUB-OPÇÃO 3
            elif sub_opt == 3:
                #   Gastos de um cliente
                cliente = buscar_cliente(clientes)
                if cliente != False:
                    vendas_from_cliente = []
                    total_gasto = 0
                    for venda in vendas:
                        if venda.get_cliente().getCPF() == cliente.getCPF():
                            total_gasto += venda.calcularTotal()
                            vendas_from_cliente.append(venda)
                    print("\nGastos do cliente", cliente.getNome())
                    for venda in vendas_from_cliente:
                        venda.exibir(False)
                        input()
                else:
                    input("Cliente não encontrado!")

                sub_opt = -1
            #SUB-OPÇÃO 4
            elif sub_opt == 4:
                #   Produto Geral
                print(" ")
                print("\nListando Produtos Cadastrados:")
                for produto in produtos:  #Para cada produto no array de produtos, exiba os dados desse produto
                print("")
                    produto.exibirDadosProduto()
                input("Pressione ENTER para continuar...")
                sub_opt = -1

            #SUB-OPÇÃO 5
            elif sub_opt == 5:
                #   Buscar produto
                produto = buscarProduto(produtos)
                if(produto != False):
                    print("")
                    produto.exibirDadosProduto()
                    input("Pressione ENTER para continuar...")
                else:
                    print("Produto não encontrado, por favor tente novamente.")
                    input("Pressione ENTER para continuar...")

                sub_opt = -1

            #SUB-OPÇÃO 6
            elif sub_opt == 6:
                #   Vendas Geral
                for venda in vendas:
                    print("\nCompra feita por:", venda.get_cliente().getNome())
                    venda.exibir(False)
                    print("")
                input()
                sub_opt = -1
            #SUB-OPÇÃO 7
            elif sub_opt == 7:
                #   Buscar Venda
                venda = buscar_venda(vendas)
                if venda != False:
                    venda.exibir(True)
                    input()
                else:
                    input("Venda não encontrada!")
                sub_opt = -1
            #SUB-OPÇÃO 8
            elif sub_opt == 8:
                #   Venda por tipo de pagamento (simples)
                tipo_pagamento = ""
                while(str.lower(tipo_pagamento) != "cheque" and str.lower(tipo_pagamento) != "cartao" and str.lower(tipo_pagamento) != "dinheiro"):
                    tipo_pagamento = input("ESCOLHA DO MÉTODO DE PAGAMENTO (Cartao, Dinheiro, Cheque): ")
                    if str.lower(tipo_pagamento) != "cheque" and str.lower(tipo_pagamento) != "cartao" and str.lower(tipo_pagamento) != "dinheiro":
                        print("Por favor escolha uma das opcões dadas: ")

                for venda in vendas:
                    if str.lower(venda.get_tipo_pagamento().getTipoPagamento()) == tipo_pagamento:
                        print("\nCompra feita por:", venda.get_cliente().getNome())
                        venda.exibir(False)
                        print("")
                input()

                sub_opt = -1
            #SUB-OPÇÃO 9
            elif sub_opt == 9:
                #   Venda por tipo de pagamento (detalhada)
                tipo_pagamento = ""
                while(str.lower(tipo_pagamento) != "cheque" and str.lower(tipo_pagamento) != "cartao" and str.lower(tipo_pagamento) != "dinheiro"):
                    tipo_pagamento = input("ESCOLHA DO MÉTODO DE PAGAMENTO (Cartao, Dinheiro, Cheque): ")
                    if str.lower(tipo_pagamento) != "cheque" and str.lower(tipo_pagamento) != "cartao" and str.lower(tipo_pagamento) != "dinheiro":
                        print("Por favor escolha uma das opcões dadas: ")

                for venda in vendas:
                    if str.lower(venda.get_tipo_pagamento().getTipoPagamento()) == str.lower(tipo_pagamento):
                        print("\nCompra feita por:", venda.get_cliente().getNome())
                        venda.exibir(True)
                        print("")
                input()
                sub_opt = -1
            #SUB-OPÇÃO 10
            elif sub_opt == 10:
                #   Voltando para o menu principal
                opt = -1

                print("voltando do submenu para o menu principal")
    elif opt == 4:
        #   Salvar Dados
        print("Começando o salvamento dos dados!")
        pickle_out = open("saved_data.pickle", "wb")
        pickle.dump({'vendas': vendas, 'clientes': clientes, 'produtos': produtos}, pickle_out)
        pickle_out.close()
        input("Okay! Tudo salvo em saved_data.pickle!")
        opt = -1
    elif opt == 5:
        #   Carregar Dados
        pickle_in = open("saved_data.pickle", "rb")
        dados_carregados = pickle.load(pickle_in)
        vendas = dados_carregados["vendas"]
        clientes = dados_carregados["clientes"]
        produtos = dados_carregados["produtos"]

        opt = -1
    elif opt == 6:
        opt = -1
        break
print("EXECUTANDO OPÇÃO", opt, "COM SUBMENU", sub_opt)
