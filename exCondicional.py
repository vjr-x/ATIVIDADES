valor= float(input("digite o valor do pedido: "))

"""
Regra de negócio:
*Se a venda for até 100 reais, não tem desconto
*Se a venda for entre 100,01 e 299,99 reais, dê 10% de desconto
*Se a venda for acima de 300 reais, dê 15% de desconto
"""

if valor <= 100:
    print(f"O valor da compra deu R${valor}.")
    exit()

elif valor > 100 and valor <= 299.99:
    desconto = 0.90

else: valor > 300
desconto = 0.85
    
total = valor * desconto

descontoPercentual = (1 - desconto) * 100
descontoPercentual = int(descontoPercentual)

#print("Valor total foi de:", total, "Seu desconto foi de", descontoPercentual)

print(f"Sua compra deu R${valor}. Você ganhou {descontoPercentual}%" \
      f" de desconto. O total agora é R${total}.")