def exibir_menu():
    print("\n~~~~~ Caderno de Tarefas ~~~~~")
    print(" 1 - Adicionar")
    print("2 - Listar")
    print("3 - Remover")
    print("0 - Sair")
    print("~~~~~~~~~~~~~~~~~~~")

def adicionar(tarefas):
    tarefa = input("Digite sua nova tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa cadastrada com sucesso!")

def listar(tarefas):
    if not tarefas:
            print("Não há tarefas para exibir!")
    else:
        for posicao_tarefa, tarefa in enumerate(tarefas, start=1):
            print(f"{posicao_tarefa} - {tarefa}")

def remover(tarefas):
    if not tarefas:
            print("Não há tarefas para remover!")
    else:
        tarefa = int(input("Digite o número da tarefa que deseja remover: "))
        if tarefa > 0 and tarefa <= len(tarefas):
            tarefa = tarefa -1
            tarefa_removida = tarefas.pop(tarefa)
            print(f"Tarefa removida: {tarefa_removida}.")
        else:
             print("Tarefa não existe, digite um número válido!")

tarefas = []

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "0": 
        break

    elif opcao == "1": adicionar(tarefas)
     
    elif opcao == "2": listar(tarefas)
    
    elif opcao == "3": remover(tarefas)

    else: print("Opção Inválida!")
