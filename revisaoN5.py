for multiplicador in range(1, 11, 1):
    resultado = multiplicador * 5
    print(f"{multiplicador} x 5 = {resultado}")



cidades = ["Blumenau", "Gaspar", "Brusque", "Penha", "Itapema"]

for cidade in cidades: 
    if cidade[0] == "B":
        continue
    print(cidade)







    produtos = ["Tenis", "Boné", "Chinelo"]
    preços = [200.00, 100.00, 50.00]
    
for posiçao, produto in enumerate(produtos):
   
    if preços[posiçao] < 150:
        preço_ajustado = round(preços[posiçao] * 1.10, 2)
        print(f"O produto {produto}, custava R${preços[posiçao]}, seu novo valor é {preço_ajustado}.")
    else:
        print(f"O produto {produto}, custa R${preços[posiçao]}.")