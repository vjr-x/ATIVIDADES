produtos = ["camiseta", "regata", "bermuda", "shorts", "calça"]
precos = [80.00, 60.00, 40.00, 45.00, 100.00]
quantidades = [2, 1, 2,0, 1]
subtotais = []

for indice, produtos in enumerate(produtos):
    preco = precos[indice] # preco = preco[0]
    quantidade = quantidades[indice]
    subtotal = quantidade * preco
    subtotais.append(subtotal)

mensagem = f"""
 ------------------------------
 Produto:{produtos}
 Quantidade:{quantidade}
 Valor unitário:{preco}
 Subtotal:{subtotal}
 ------------------------------ 
"""

print(mensagem)
print(f"O total da compra deu: R$ {sum(subtotais)}.")
print(subtotais)
