def menu_temperatura():

    print('Cálculo da Temperatura na Cabeca do Poco:\n')

    print('1. Temperatura a Montante')
    print('2. Temparatura a Jusante')
    print('0. Voltar ao Menu Principal\n')
    
    escolher_opcao_menu_temperatura()

def escolher_opcao_menu_temperatura():
    try:
        opcao_escolhida_menu_temperatura = int(input('Escolha uma opcao: '))
        match opcao_escolhida_menu_temperatura:
            case 1:
                os.system('cls')
                calcular_temperatura_montante()
            case 2:
                os.system('cls')
                calcular_temperatura_jusante()
            case 0:
                os.system('cls')
                menu_inicial()
            case _:
                opcao_invalida()
                menu_temperatura()
    except:
        opcao_invalida()
        menu_temperatura()

def calcular_temperatura_montante(lim_critico):

    match lim_critico:
        case 0:
            print('\nOcorreu um erro ao determinar o tipo de fluxo. Por favor, tente novamente')
            calcular_limite_critico()
        case 1: #Fluxo sub-crítico
            
        case 2: #Fluxo crítico

        case _:
            print('\nOcorreu um erro ao determinar o tipo de fluxo. Por favor, tente novamente')
            calcular_limite_critico()
    print('Calculo da Temperatura a Montante')
    calcular_limite_critico()
    T2 = input('Insira a temperatura a jusante (T2): ')
    Z1 = input('Insira o fator de compressibilidade a montante (Z1): ')
    Z2 = input('Insira o fator de compressibilidade a jusante (Z2): ')
    P1 = input('Insira a pressao a montante (P1): ')
    P2 = input('Insira a pressao a jusante (P2): ')    
    T1 = T2/((Z1/Z2)*(P1/P2)**((k-1)/k))

def calcular_temperatura_jusante():
    
    print('Calculo da Temperatura a Jusante')




