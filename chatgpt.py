# Declarando variável float vazia
valor = None

# Solicitando entrada do usuário e tratando possíveis erros
while True:
    try:
        valor = float(input("Insira um valor: "))
        break  # Se a conversão for bem-sucedida, saia do loop
    except ValueError:
        print("Erro: Por favor, insira um número válido.")

# Agora, você pode usar o valor inserido pelo usuário
print("Valor inserido:", valor)