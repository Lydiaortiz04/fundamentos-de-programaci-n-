matriz_a = [
    [15, 8],
    [23, 12]
]
# Empezamos asumiendo que el primero es el mayor \
mayor = matriz_a[0][0] # Empiezo con 15 
# Recorreremos toda la matriz
for fila in matriz_a:
    for elemento in fila:
        if elemento > mayor: # Si encuentro uno mas grande
            mayor = elemento # Lo guardo como el nuevo mayor 

# Mostramos resultado
print("La matriz es:")
for fila in matriz_a:
    for elemento in fila:
        print(elemento, end=" ")
    print()
print(f"\nEl numero mayor es: {mayor}")
