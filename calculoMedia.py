import math

nota1 = float(input("Digite a nota do aluno: "))
nota2 = float(input("Digite a nota do aluno: "))
nota3 = float(input("Digite a nota do aluno: "))

média =(nota1 + nota2 + nota3) / 3
média = math.ceil(média)
# Aqui outra forma de arrebondar:
média = round( média, 2)
# Forma de arrebondar valores após a virgula:

print("A média foi de:", média)

if média >= 0 and média <= 5.5:
    print("Reprovado")

elif média > 5.5 and média <= 6.5:
    print("Recuperação") 

elif média > 7.0 and média <= 10:
    print ("Aprovado")

else:
    print("Número não condiz com uma nota de 0 a 10")  