def exibir_menu():
    print("\n~~~~~ MENU ~~~~~")
    print(" 1 - Bem vindo!")
    print("2 - Sobre o curso.")
    print("3 - Ajuda.")
    print("0 - Sair.")
    print("~~~~~~~~~~~~~~~~")

def saudacao():
    nome = input("Digite seu nome: ")
    print(f"Seja bem vindo ao curso, {nome}!")

def sobre():
    print("O curso Jovem Programador prepara novos talentos para o mercado da tecnologia!")

def ajuda():
    print("Esse programa cria um menu infinito usando While para reproduzir frases!")


while True:

    exibir_menu()
    opcao = input("Escolha a opção: ")

    if opcao == "0":
        break

    elif opcao == "1":
        saudacao()

    elif opcao == "2":
        sobre()

    elif opcao == "3":
        ajuda()