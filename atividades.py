
valor = 100
desconto = 10
total = valor- desconto
print("O total é:", total)

valor= float(input("digite o valor do pedido: "))


if valor >= 100:
    valor = valor * 0.90
    print("Valor total foi de:", total)

else:
    total = valor *1.10
    print("valor total foi de:", total)