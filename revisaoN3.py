nota = 8
falta = 12

if nota >= 7 and falta <= 16:
    print("Aprovado")

else :
    print("Reprovado")






numero = int(input("Digite um numero:"))

if numero > 0:
    print("Positivo")

elif numero < 0:
    print("Negativo")

else:
    print("É ZERO")





usuario_correto = "admin" 
senha_correta = "1234"
usuario = input("Digite usuario:")
senha = input("Digite senha:")

if usuario == usuario_correto and senha == senha_correta :
    print("Acesso permitido!")

else:
    print("Usuario ou senha inválidos.")



