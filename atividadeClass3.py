'''
A classe Aluno
- Crie a classe alunos com nome e nota
- Crie 2 alunos com valores diferentes
- imprima o nome e a nota de cada um

2 parte
- reaproveite a classe aluno, crie o metodo 'situacao()'
- se a nota for >=6, mostre aprovado
- Caso contrario, mostre reprovado
- teste com os 2 alunos diferentes

'''

class Alunos():
    def __init__(self, nome: str, nota: float):
        self.nome = nome
        self.nota = nota
        
    def situacao(self):
        if self.nota >= 6:
            return "Aprovado " 
                
        else:
            return 'Reprovado'
        
    def exibir(self):        
        print(f'Nome: {self.nome}, Nota: {self.nota} - Situacao {self.situacao()}')

'''
aluno01 = Alunos("Fabio", 5.0)
aluno02 = Alunos("Fabiana", 8.0)


print('='*45 )
aluno01.exibir()
print('='*45 )
aluno02.exibir()
print('='*45 )
'''
def menu_simples():
    print('='*30)
    print(f'\n{'Cadastro de alunos':^30}')
    print('\n(1) - Cadastro')   
    print('(2) - Listar alunos e Situacao')
    print('(0) - Sair')
    print('\n' +'='*30)

def cadastrar_alunos():
    print('\nCadastrando ALuno')
    nome = input('Digite seu nome: ')
    nota = float(input('Digite sua nota: '))
    novo_aluno = Alunos(nome, nota)
    lista_de_alunos.append(novo_aluno)
    print(f'{nome} e {nota:.2f} adicionado com sucesso. ')

def listar_alunos():
    print(f'\n{'Listando Aluno':^30}')
    if not lista_de_alunos:
        print('Nao esta na lista. ')
        
    else:
        for i in lista_de_alunos:
            i.exibir()
    print('=-'*30)
    


lista_de_alunos = []

while True:
    menu_simples()
    Opcao = input('Digite sua opcao: ')

    if Opcao == '0':
        break

    elif Opcao == '1':
        cadastrar_alunos()

    elif Opcao == '2':
        listar_alunos()

    else:
        print('Opcao invalida')