n = int(input("Introduce un número: "))
suma = 0

for i in range(1, n+1):
    suma += i

print(f"La suma de los números del 1 al {n} es: {suma}")