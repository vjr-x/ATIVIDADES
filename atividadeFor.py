frutas = ["maça", "banana", "açai", "abacaxi", "maracuja"]
#Entrada do usuario pedindo para digitar nome da fruta favorita
fruta_favorita = input("qual sua fruta favorita?:")

#SE a a fruta favorita NÃO ESTÁ NA lista frutas
if fruta_favorita not in frutas:
    print("sua fruta favorita não está na lista de frutas")
    #Faça isso (exibir mensagem e sai do sistema):
    
    #PARA cada posição (índice) e fruta NA lista numerada

for posicao, fruta in enumerate(frutas):
    #Faça isso:
    #SE a fruta dessa iteração é igual a fruta favorita
     if fruta == fruta_favorita:
        # Salva numa nova variável a posição dessa iteração
        posicao_fruta_favorita = posicao
        #Quebra o for (faz ele parar)
        break

#Saída do algoritmo (print)
print (f"Minha fruta favorita está na posição índice{posicao_fruta_favorita}")