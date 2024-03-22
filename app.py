import os

def exibir_nome_do_programa():

    print('Bem vindo ao Wellhead Analyzer!\n')

    menu_inicial()

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
                menu_pressao()
            case 3:
                os.system('cls')
                menu_vazao()
            case 0:
                finalizar_app()
            case _:
                opcao_invalida()
                menu_inicial()                                    
    except:
        opcao_invalida()
        menu_inicial()
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

def opcao_invalida():
    os.system('cls')
    print('Opcao invalida!\n')

def finalizar_app():
    os.system('cls')
    print('Tem certeza que voce gostaria de finalizar o aplicativo?\n')

    print('1. Sim')
    print('2. Nao, voltar ao menu inicial\n')

    escolher_opcao_finalizar_app()

def escolher_opcao_finalizar_app():
    
    opcao_escolhida_finalizar_app = int(input('Escolha uma opcao: '))
    match opcao_escolhida_finalizar_app:
        case 1:
            exit()
        case 2:
            os.system('cls')
            menu_inicial()
        case _:
            opcao_invalida()
            escolher_opcao_finalizar_app()

def menu_temperatura():

    print('Cálculo da Temperatura na Cabeca do Poco:\n')

    print('1. Temperatura a Montante')
    print('2. Temparatura a Jusante')
    print('0. Voltar ao Menu Principal\n')
    
    escolher_menu_temperatura()

def escolher_menu_temperatura():
    try:
        opcao_escolhida_temperatura = int(input('Escolha uma opcao: '))
        match opcao_escolhida_temperatura:
            case 1:
                os.system('cls')
                calcular_temp_montante()
            case 2:
                os.system('cls')
                calcular_temp_jusante()
            case 0:
                os.system('cls')
                menu_inicial()
            case _:
                opcao_invalida()
                menu_temperatura()
    except:
        opcao_invalida()
        menu_temperatura()

def calcular_temp_montante():

    print('Calculando a temperatura a montante')
    
def calcular_temp_jusante():
    
    print('Calculando a temperatura a jusante')

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

def main():
    os.system('cls')
    exibir_nome_do_programa()

if __name__ == '__main__':
    main()