def exibir_menu():
    print("\n~~~~~ Conversor de Unidades ~~~~~")
    print(" 1 - celsius -> fahrenheit")
    print("2 - reais -> dólares")
    print("3 - horas -> minutos")
    print("0 - Sair.")
    print("~~~~~~~~~~~~~~~~")



def conversao1():
    celsius = float(input("Digite o valor em Celsius que deseja converter: "))
    fh = celsius * 1.8 + 32
    print(f"{celsius} graus celsius para fahrenheit = {fh}")

def conversao2():
    reais = float(input("Digite o valor em R$ que deseja converter: "))
    dolares = reais / 5
    print(f"O total deu U${dolares}")

def conversao3():
    horas = float(input("Digite a quantidade de horas que deseja converter: "))
    minutos = horas * 60
    print(f"São {minutos} minutos.")

while True:

    exibir_menu()
    opcao = input("Escolha a opção: ")

    if opcao == "0": break

    elif opcao == "1": conversao1()

    elif opcao == "2": conversao2()

    elif opcao == "3": conversao3()

    else: print("Opção Inválida!")
