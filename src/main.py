import platform
import os


def clear_screen():
    if platform.system() == 'Linux' or platform.system() == 'Dawrin':
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
        if sub_opt == 1:
            #   Cadastro de Cliente
            pass
        elif sub_opt == 2:
            #   Cadastro de Produto
            pass
        elif sub_opt == 3:
            #   Voltando para o menu principal
            opt = -1
            sub_opt = -1
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
            pass
        elif sub_opt == 2:
            #   Buscar Cliente
            pass
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
