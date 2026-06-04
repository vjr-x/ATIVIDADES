def exibir_menu():
    print("\n~~~~~ Conta Bancária ~~~~~")
    print(" 1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver saldo")
    print("0 - Sair")
    print("~~~~~~~~~~~~~~~~~~~")

def depositar(saldo):
    valor = int(input("Quanto você deseja depositar? "))
    saldo_atualizado = valor + saldo
    print(f"Seu saldo agora está em: {saldo_atualizado}")

saldo = 0.0

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "0": 
        break

    elif opcao == "1": depositar(saldo)
     
    elif opcao == "2": sacar(saldo)
    
    elif opcao == "3": ver_saldo(saldo)

    else: print("Opção Inválida!")