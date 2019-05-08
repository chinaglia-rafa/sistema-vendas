import platform
import os
from cliente import *
from item import *
from pagamento import *
from produtos import *
from vendas import *


#DEFINIÇÃO DE LISTAS DE ARMAZENAMENTO
clientes = []
produtos = []
vendas = []

print(platform.system())
def clear_screen():
    if platform.system() == 'Linux' or platform.system() == 'Darwin':
        os.system('clear')
    else:
        os.system('cls')


def buscar_cliente(lista_clientes):
    busca = "nada"

    while(str.lower(busca) != "cpf" and str.lower(busca) != "nome"):
        busca = input("Deseja buscar o cliente por CPF ou Nome? ")
        if(str.lower(busca) == "cpf"):
            cpf = input("Digite o CPF que deseja buscar: ")
            for cliente in clientes:
                if(cliente.getCPF() == cpf):
                    return cliente
            return False
        elif(str.lower(busca) == "nome"):
            nome = input("Digite o Nome que deseja buscar: ")
            for cliente in clientes:
                if(str.lower(cliente.getNome()) == str.lower(nome)):
                    return cliente
            return False
        else:
            print("Por favor, escolha uma das opções disponíveis!")


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
sub_opt = -1

# v = vendas('123', dinheiro(), cliente('400.971.138-83', 'Rafael Araújo Chinaglia'))

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
        # EM ANDAMENTO
        aux = 0
        opcao = "nada"
        while(aux != 1 and opcao != "nao"):
            yes_or_no = "nada"
            tipo_pagamento = "nada"
            numero = input("Digite o numero da compra: ")
            cpf = input("Qual o CPF do cliente que fez a compra? ")

            #Verifica o tipo de pagamento e pede os dados necessarios
            while(str.lower(tipo_pagamento) != "cheque" and str.lower(tipo_pagamento) != "cartao" and str.lower(tipo_pagamento) != "dinheiro"):
                print("ESCOLHA DO MÉTODO DE PAGAMENTO")
                tipo_pagamento = input("Qual o tipo de pagamento? ")
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
                    print("Por favor escolha uma das opcões dadas: ")



            for cliente in clientes: #BUSCA O CPF
                print("a")
                if(cliente.getCPF() == cpf):
                    cliente_cadastro = cliente
                    aux = 1
            if(aux == 1): #SE O CPF FOI ENCONTRADO
                compra = venda(numero, payment, cliente_cadastro)
                vendas.append(compra)
                opt = -1
            else: #CPF NAO ENCONTRADO
                while(str.lower(yes_or_no) != "sim" and str.lower(yes_or_no) != "nao"):
                    yes_or_no = input("CPF não encontrado, deseja tentar novamente? (SIM, NAO): ")
                    yes_or_no = str.lower(yes_or_no)
                    if(str.lower(yes_or_no) != "sim" and str.lower(yes_or_no) != "nao"):
                        print("Por favor, escolha uma das opções dadas!")


        opt = -1


    elif opt == 3:
        #   Relatórios
        sub_opt = -1
        while sub_opt == -1:
            sub_opt = menu_relatorios()
            #SUB-OPÇÃO 1
            if sub_opt == 1:
                #   Lista de Clientes
                for cliente in clientes:   #Para cada item no array que guarda os clientes, utilize a função de exibir os dados do cliente
                    cliente.exibirCliente()
                input("Pressione ENTER para continuar...")
                sub_opt = -1
            #SUB-OPÇÃO 2
            elif sub_opt == 2:  # TODO: adicionar loop de tentar novamente
                #   Buscar Cliente
                cliente = buscar_cliente(clientes)
                if cliente != False:
                    cliente.exibirCliente()
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
                else:
                    input("Cliente não encontrado!")

                sub_opt = -1
            #SUB-OPÇÃO 4
            elif sub_opt == 4:
                #   Produto Geral
                for produto in produtos:  #Para cada produto no array de produtos, exiba os dados desse produto
                    print(" ")
                    print("INFORMAÇÕES DO PRODUTO:")
                    produto.exibirDadosProduto()
                input("Pressione ENTER para continuar...")
                sub_opt = -1
            #SUB-OPÇÃO 5
            elif sub_opt == 5:
                #   Buscar produto
                busca = "nada"
                while(str.lower(busca) != "codigo" and str.lower(busca) != "descricao"):
                    busca = input("Você deseja buscar o produto através do código ou da descrição? ")
                    if(str.lower(busca) == "codigo"):
                        codigo = input("Digite o código do produto: ")
                        for produto in produtos:
                            if(produto.getCodigo() == codigo):
                                produto.exibirDadosProduto()
                                input("Pressione ENTER para continuar...")
                    elif(str.lower(busca) == "descricao"):
                        descricao = input("Digite a descrição do produto: ")
                        for produto in produtos:
                            if(produto.getDescricao() == descricao):
                                produto.exibirDadosProduto()
                                input("Pressione ENTER para continuar...")
                    else:
                        print("Por favor, escolha uma das opções disponíveis!")
                sub_opt = -1

            #SUB-OPÇÃO 6
            elif sub_opt == 6:
                #   Vendas Geral
                sub_opt = -1
            #SUB-OPÇÃO 7
            elif sub_opt == 7:
                #   Buscar Venda
                sub_opt = -1
            #SUB-OPÇÃO 8
            elif sub_opt == 8:
                #   Venda por tipo de pagamento (simples)
                sub_opt = -1
            #SUB-OPÇÃO 9
            elif sub_opt == 9:
                #   Venda por tipo de pagamento (detalhada)
                sub_opt = -1
            #SUB-OPÇÃO 10
            elif sub_opt == 10:
                #   Voltando para o menu principal
                opt = -1

                print("voltando do submenu para o menu principal")
    elif opt == 4:
        #   Salvar Dados
        opt = -1
    elif opt == 5:
        #   Carregar Dados
        opt = -1
    elif opt == 6:
        opt = -1
        break
print("EXECUTANDO OPÇÃO", opt, "COM SUBMENU", sub_opt)
