def menu_inicial():

    print('O que você gostaria de calcular?\n')

    print('1. Temperatura')
    print('2. Pressao')
    print('3. Vazao')
    print('0. Finalizar aplicativo\n')

    escolher_opcao_menu_inicial()

def escolher_opcao_menu_inicial():
    try:
        opcao_escolhida_menu_inicial = int(input('Escolha uma opcao: '))
        match opcao_escolhida_menu_inicial:
            case 1:
                os.system('cls')
                menu_temperatura()

            case 2:
                os.system('cls')
                print('Cálculo da Pressao na Cabeca do Poco:')
            case 3:
                os.system('cls')
                print('Cálculo da Vazao na Cabeca do Poco:')
            case 0:
                finalizar_app()
            case _:
                opcao_invalida()
                menu_inicial()                                    
    except:
        opcao_invalida()
        menu_inicial()