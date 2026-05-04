idade= int(input("digite sua idade: "))
if idade >= 0 and idade <= 12:
    print("criança")

elif idade >= 12 and idade <= 17:
    print("adolescente")

elif idade >= 17 and idade <= 50:
    print("jovem adulto")

else:
    print("idoso")