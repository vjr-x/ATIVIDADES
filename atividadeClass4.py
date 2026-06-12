class Aluno:
    def __init__(self, nome, notas=[]):
        self.nome = nome
        self.notas = notas
        
    def exibir(self):
        print(f"Aluno: {self.nome}")
        if self.notas:
            for ordem_nota, nota in enumerate(self.notas, 1):
                print(f"{ordem_nota}: {nota}")

    def situacao(self):
        #Aqui voces vao fazer a logica de somas: 
         self.notas
         #... e fazer o cálculo da média.
         #por fim, dizer se está aprovado ou reprovado.

    def exibir_menu():
        print('='*30)
        print('\n 1 - Cadastrar alunos')   
        print('2 - Lançar notas')
        print('3 - Ver situação')
        print('4 - Listar alunos')
        print('0 - Sair')
        print('\n' +'='*30)

#Opção 1
def cadastrar_alunos():
    nome = input("Digite o nome do aluno: ")
    aluno = Aluno(nome)
    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso!")

#Opção 2 
def lancar_nota():
    indice = int(input("Digite o código do aluno: ")) # 0
    aluno = alunos[indice] # aluno("Daniel, []")
    nota =     
alunos = []

while True:
    exibir_menu()
    opcao = input("Escolha a opção")

    if opcao == '0':
        break

    elif opcao == '1':
        cadastrar_aluno()

    elif opcao == '2':
        ...

    elif opcao == '3':
        ...

    else:
        print('Opcao invalida')
