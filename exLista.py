pdtloja = ["camiseta", "regata", "bermuda", "shorts", "calça"]
precos = [80.00, 60.00, 40.00, 45.00, 100.00]
print(pdtloja)
print(pdtloja[0]) 
print(pdtloja[-1])
print(len(pdtloja))

#Para exibir:
print(f"O produto {pdtloja[0]} custa R${precos[0]}.")

#Para remover o último produto e preço também:
pdtloja.remove(pdtloja[-1])
precos.remove(precos[-1])

#Para somar o preço de todos os produtos:
total = sum(precos)
print(f"O total deu R${total}")

#Lógica condicional if/else para desconto:
if total < 100:
    exit()
else:
 desconto =0.95
 total = total * desconto
 print(f" O total agora com desconto é de R${total}")
