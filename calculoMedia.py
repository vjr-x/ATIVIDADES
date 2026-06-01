import math

def calcular_media(notas: list) -> float:
    media = sum(notas) / len(notas)
    return math.ceil(média)

contador = 1
notas = []

while True:
    nota = float(input(f"Digite a nota {contador} ou -1 para sair: "))
    
    if nota == -1:
        break

    notas.append(nota)
    print("Nota registrada!")

media = calcular_media(notas)
print("A média foi de: ", media)

if média >= 0 and média <= 5.5:
    print("Reprovado")

elif média > 5.5 and média <= 6.5:
    print("Recuperação") 

elif média > 7.0 and média <= 10:
    print ("Aprovado")

else:
    print("Número não condiz com uma nota de 0 a 10")  