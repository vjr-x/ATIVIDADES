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
    
    if escolha == "1":
        total = n1 + n2
        print(f"{n1} + {n2} = {total}") 
    elif escolha == "2":
        total = n1 - n2
        print(f"{n1} - {n2} = {total}")
    elif escolha == "3":
        total = n1 * n2
        print(f"{n1} * {n2} = {total}")
    elif escolha == "4":
        if n2 == 0:
            print("Não é possivel dividir por 0.")
        else:
            print(f"{n1} / {n2} = {n1 / n2}")
    else:
        print("Opção inválida!")
     