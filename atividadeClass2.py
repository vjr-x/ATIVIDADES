class Produto():
    def __init__(self, nome: str, preco: float, qtd: int):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

    def exibir(self):
        print(f'produto: {self.nome}, preco R$:{self.preco:.2f}, qtd {self.qtd} unidades.')

def menu_simples ():
    print('='*30 )    
    print(f'\n{"Cadastro de produtos ":^30}')  
    print(' 1 - Cadastro do produto')   
    print(' 2 - Listar produtos')
    print(' 0 - SAIR\n')
    print('='*30 )
    
def listar_produtos():
    print(f'\n{"Lista de produtos ":^30}')
    if not lista_de_produtos:
        print('Nenhum produto cadastrado.')
    else:
        for produto in lista_de_produtos:
            produto.exibir() 
    print('='*30 + '\n')



def cadastrar_produto():
    print('\nCADASTRANDO PRODUTO ')
    nome = input('Digite o produto: ')
    preco = float(input('Digite o preco do produto: '))
    qtd = int(input('Digite a quantidade de produto: '))
    novo_produto = Produto(nome, preco, qtd)
    lista_de_produtos.append(novo_produto)
    print(f'{nome} cadastrado com sucesso!\n')


lista_de_produtos = []
while True:
    menu_simples()

    opcao = input('Digite sua opcao. ')

    if opcao == "0":
        break
    elif opcao == '1':
        cadastrar_produto()

    elif opcao == '2':
        listar_produtos()

    else:
        print('Opcao invalida')
    