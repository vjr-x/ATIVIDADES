produtos = ["pneu", "óleo", "relacao"]
preços_produtos = [149.99, 39.99, 85.99]
serviços = ["troca de óleo", "ajuste no freio", "revisão completa"]
preços_serviços = [79.97, 24.99, 179.99]

cliente = input("Você deseja ver nossos Produtos ou Serviços?" )

if "produtos" :
    for posiçao, produto in enumerate(produtos):
        print (f"O {produto} custa {preços_produtos[posiçao]}.")
elif "serviços" :
    for indice, serviço in enumerate(serviços):
        print (f"O {serviço} custa {preços_serviços[indice]}.")
else:
    print ("Desculpe não trabalhamos com isso!")