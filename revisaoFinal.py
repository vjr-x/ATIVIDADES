produtos = ["pneu", "óleo", "filtro de óleo"]
preços_produtos = [149.99, 49.99, 35.99]
serviços = ["troca de óleo", "ajuste no freio", "revisão completa"]
preços_serviços = [79.97, 24.99, 179.99]

print("Bem vindo a Auto-Peças!")
escolha = input("Você deseja ver nossos Produtos ou Serviços?" )

if escolha == "produtos":
    for indice, produto in enumerate(produtos):
        print (f"{produto} custa R${preços_produtos[indice]}.")
      
elif escolha == "serviços":
    for indice, serviço in enumerate(serviços):
        print (f"{serviço} custa R${preços_serviços[indice]}.")
        
else:
    print ("Desculpe não trabalhamos com isso!")
    exit()

codigo = int(input("Digite o código do item desejado: "))

if escolha == "produtos":
    nome_esc = produtos[codigo]
    preço_esc = preços_produtos[codigo]

elif escolha == "serviços":
    nome_esc = serviços[codigo]
    preço_esc = preços_serviços[codigo]

if preço_esc >= 300:
    preco_esc = round(preço_esc * 0.90, 2)

mensagem = f"""
===========================
Item: {nome_esc}
Preço: {preço_esc}
===========================
"""

print(mensagem)