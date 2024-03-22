def menu_vazao():

    print('Cálculo da Vazao na Cabeca do Poco:\n')

    print('1. Modelo Empirico')
    print('2. Sachdeva et al.')
    print('0. Voltar ao Menu Principal\n')
    
    escolher_opcao_menu_vazao()

def escolher_opcao_menu_vazao():
    try:
        opcao_escolhida_menu_vazao = int(input('Escolha uma opcao: '))
        match opcao_escolhida_menu_vazao:
            case 1:
                os.system('cls')
                calcular_vazao_empirico()
            case 2:
                os.system('cls')
                calcular_vazao_sachdeva()
            case 0:
                os.system('cls')
                menu_inicial()
            case _:
                opcao_invalida()
                menu_vazao()
    except:
        opcao_invalida()
        menu_vazao()

def calcular_vazao_empirico():

    print('Calculo da Vazao atraves dos Modelos Empiricos')

def calcular_vazao_sachdeva():
    
    print('Calculo da Vazao atraves da Correlacao de Sachdeva et al.')