
while True:
    try:
        numero1 = int(input("Ingrese el primer número: "))
        break
    except ValueError:
        print("Por favor, ingrese un número válido.")

while True:
    try:
        numero2 = int(input("Ingrese el segundo número: "))
        break
    except ValueError:
        print("Por favor, ingrese un número válido.")

print(f"Los numeros ingresados son: {numero1} y {numero2}")

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
elevacion = numero1 ** numero2


print(f"La suma es igual a: {suma}")
print(f"La resta es igual a: {resta}")
print(f"La multiplicación es igual a: {multiplicacion}")
print(f"La división es igual a: {division}")
print(f"la elevacion es iguala: {elevacion}")