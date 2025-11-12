print("\n Ejercicio 6: Desafio\n")

numeros_ej6 = [12, 5, 9, 2, 15]
print("Original:\n", numeros_ej6)
n = len(numeros_ej6)

for i in range (n):
    for j in range(0, n - i - 1):
        if numeros_ej6[j] < numeros_ej6[j + 1]: # que va aqui?
            numeros_ej6[j], numeros_ej6[j + 1] = numeros_ej6[j + 1], numeros_ej6[j]