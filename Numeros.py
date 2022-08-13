conjunto = []
cantidad = int(input("Cantidad: "))
mayor = 0
menor = 0
i = 1
cont = "s"
while(cantidad > 0):
    numero = float(input("Numero #" + str(i) + ": "))
    conjunto.append(numero)
    i = i + 1
    cantidad = cantidad - 1
mayor = max(conjunto)
menor = min(conjunto)

print("Conjunto: ", conjunto)
print("Mayor: ", mayor)
print("Menor: ", menor)
cont = input("Desea continuar")
