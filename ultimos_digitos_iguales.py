"""PROGRAMA
DE SABER SI LOS DOS ULTIMOS DIGITOS DE UN ENTERO SON IGUALES"""

print("---------------------------")
print("--ultimos digitos iguales--")
print("---------------------------")

x = int(input("ingrese el numero: "))

ultimo_digito = x % 10
penultimo_digito = (x % 100) // 10

if ultimo_digito == penultimo_digito:
    print("El numero tiene sus dos ultimos digitos iguales")
else:
    print("El numero no tiene sus dos ultimos digitos iguales")

    