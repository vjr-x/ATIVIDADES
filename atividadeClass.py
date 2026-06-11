class Produto():
    def __init__(self, nome: str, preco: float, qtd: int):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

    def exibir(self):
        print(f'produto: {self.nome}, preco R$:{self.preco:.2f}, qtd {self.qtd} unidades.')

#primeira forma de fazer
produto_01 = Produto("Arroz", 10.00, 15)

#segunda forma de fazer
produto_02 = Produto(nome="feijao", preco=9.0, qtd=9) #esse igual passa a quantidade ja definida.



produto_01.exibir()