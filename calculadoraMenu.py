def somar(n1, n2):
    total = n1 + n2
    print(f"{n1} + {n2} = {total}") 

def subtrair(n1, n2):
    total = n1 - n2
    print(f"{n1} - {n2} = {total}")

def multiplicar(n1, n2):
    total = n1 * n2
    print(f"{n1} * {n2} = {total}")

def dividir(n1, n2):
    if n2 == 0: print("Não é possivel dividir por 0.")
    else: print(f"{n1} / {n2} = {round(n1 / n2, 2)}")

while True:

    menu = """
    ===== CALCULADORA =====
    1- Soma (+)
    2- Subtração (-)
    3- Multiplicação (*)
    4- Divisão (/)
    0- Sair
    """
    print(menu)
    escolha = input("Digite a opção: ")
    
    if escolha == "0":
        break

    if escolha not in ["1", "2", "3", "4", "0"]:
        print(("Opção inválida! Tente novamente!"))
        continue

    n1 = int(input(f"Digite o primero número: "))
    n2 = int(input(f"Digite o segundo número: "))
    
    if escolha == "1": somar(n1, n2)
    elif escolha == "2": subtrair(n1, n2)
    elif escolha == "3": multiplicar(n1, n2)
    elif escolha == "4": dividir(n1, n2)
    else:
        print("Opção inválida!")
     