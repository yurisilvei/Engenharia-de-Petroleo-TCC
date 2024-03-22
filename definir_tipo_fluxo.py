import os

os.system('cls')


def calcular_limite_critico():

    # Solicitar valores de Cp e Cv
    while True:
        try:
            c_p = float(input('Insira o valor do calor especifico a pressao constante (Cp): '))
            break  # Se a conversão for bem-sucedida, saia do loop
        except ValueError:
            print("Erro: Por favor, insira um número válido.")
    while True:
        try:
            c_v = float(input('Insira o valor do calor especifico a volume constante (Cv): '))
            break  # Se a conversão for bem-sucedida, saia do loop
        except ValueError:
            print("Erro: Por favor, insira um número válido.")

    k = c_p/c_v
    lim_critico = (2/(k+1))**(k/(k-1))

    print(f'\nO valor da razao k é {k} e o limite critico e {lim_critico:.3f}')
    print(f'Portanto o (P1/P2)crit é {lim_critico:.3f}\n')

    definir_tipo_fluxo(lim_critico)

def definir_tipo_fluxo(lim_critico):

    # Definimos a variável tipo_fluxo que pode possuir 3 valores:
    # 0 - O tipo de fluxo não foi definido
    # 1 - Fluxo subcrítico
    # 2 - Fluxo crítico
    tipo_fluxo = 0

    # Solicitar valores de pressão a montante (P1) e a jusante (P2)
    while True:
        try:
            P1 = float(input('Insira o valor da pressão a montante (P1): '))
            break # Se a conversão for bem-sucedida, saia do loop
        except ValueError:
            print('Erro: Por favor, insira um número válido.')
    while True:
        try:
            P2 = float(input('Insira o valor da pressão a jusante (P2): '))
            break # Sea a conversão for bem-sucedida, saia do loop
        except ValueError:
            print('Erro: Por favor, insira um número válido.')
    
    razao_pressoes = P2 / P1

    # Verificar o tipo de fluxo com base na razão das pressões
    if razao_pressoes > 1:
        print('\nO escoamento segue do interior do poço para fora dele, portanto, a pressão a montante deve ser maior que a pressão a jusante')
    elif 1 >= razao_pressoes >= lim_critico:
        print('\nA razão entre as pressões é maior que o limite crítico, portanto o fluxo é subcrítico')
        tipo_fluxo = 1
    elif lim_critico > razao_pressoes:
        print('\nA razão entre as pressões é menor que o limite crítico, portanto o fluxo é crítico')
        tipo_fluxo = 2
    else:
        print("\nOcorreu um erro ao determinar o tipo de fluxo. Por favor, verifique as entradas.")

calcular_limite_critico()