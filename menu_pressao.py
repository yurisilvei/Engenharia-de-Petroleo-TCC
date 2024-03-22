def menu_pressao():

    print('Cálculo da Pressao na Cabeca do Poco:\n')

    print('1. Pressao a Montante')
    print('2. Pressao a Jusante')
    print('0. Voltar ao Menu Principal\n')
    
    escolher_opcao_menu_pressao()

def escolher_opcao_menu_pressao():
    try:
        opcao_escolhida_menu_pressao = int(input('Escolha uma opcao: '))
        match opcao_escolhida_menu_pressao:
            case 1:
                os.system('cls')
                calcular_pressao_montante()
            case 2:
                os.system('cls')
                calcular_pressao_jusante()
            case 0:
                os.system('cls')
                menu_inicial()
            case _:
                opcao_invalida()
                menu_pressao()
    except:
        opcao_invalida()
        menu_pressao()

def calcular_pressao_montante():

    print('Calculo da Pressao a Montante')

def calcular_pressao_jusante():
    
    print('Calculo da Pressao a Jusante')