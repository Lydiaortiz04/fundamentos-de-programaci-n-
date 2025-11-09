print("\nEjercicio1: Tbala de multiplicar")

numero = 5
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")


print("\nEjercicio2")
numeros = [10, 20, 30, 40, 50]
suma = 0
for num in numeros:
    suma += num
print(f"La suma de los números es: {suma}")



texto = "Alo, que haciendo mi gente en miercoles"
contador = 0
for letra in texto:
    if letra.lower() in 'aeiou':
        contador += 1
print (f"Hay {contador} vocales.")

print("\nEjercicio4")

numeros = [15, 42, 8, 23, 67, 31]
mayor = numeros[0] # Empezamos con el primero de la lista
for num in numeros:
    if num > mayor:
        mayor = num
print(f"El número mayor es: {mayor}")


print("\nEjercicio5")

cuadrados = []
for i in range(1, 6):
    cuadrados.append(i ** 2)
print(cuadrados)
