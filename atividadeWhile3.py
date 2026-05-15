contador = 0    #Contador recebe 0.
numeros = ()    #Numeros recebe lista vazia.
numero = -1     #Numero recebe -1

while numero != 0:     #Enquanto numero for diferente de 0:
    numero = int(input("Digite um número (0 para sair):"))    #Pergunte "digite um numero" e converta para inteiro
    #Numero recebe o que o usuario digitou

    if numeros != 0:     #Se o numero for diferente de:
        contador = contador + 1     #Contador recebe contador +1.
        numero = numeros.append    #Numero é adicionado em lista numero.
print(f"Após {contador} tentativas, você digitou 0.")      #Exibe numero de tentativas antes do 0.
