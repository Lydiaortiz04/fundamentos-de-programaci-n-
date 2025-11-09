print("\nEjercicio2\n")
amigos = []

print("Lista inicial", amigos)

amigos.append("Juan")
print("Después de agregar a Juan:", amigos)

amigos.append("María")
print("Después de agregar a María:", amigos)

amigos.append("Pedro")
print("Después de agregar a Pedro:", amigos)

print(f"\ntotal de amigos: {len(amigos)}\n")




print("\nEjercicio3\n")
calificaciones = [98, 90, 88, 92, 89]

# Mostrar todas las calificaciones
print("Calificaciones:", calificaciones)

# Calcular el promedio 
suma = sum(calificaciones)
promedio = suma / len(calificaciones)
print(f"Promedio: {promedio}")

# Encontrar la mejor y peor calificación
mejor = max(calificaciones)
peor = min(calificaciones)
print(f"Mejor calificación: {mejor}")
print(f"Peor calificación: {peor}")


print("\nEjercicio4\n")
carrito = []
# Agregar productos
print("Agregando productos al carrito...")
carrito.append("Iphone 15")
carrito.append("Airpods")
carrito.append("funda")
carrito.append("cargador")

print("Carrito actual:", carrito)
print(f"Productos en el carrito: {len(carrito)}")

# Decidiste que no quieres la funda
print("\nEliminando la funda...")
carrito.remove("funda")

print("carrito final:", carrito)
print(f"Total de productos: {len(carrito)}")


print("\nEjercicio5\n")

videojuegos = ["Minecraft", "Fortnite",
               "Valorant", "roblox", "GTA V"]

print("MI TOP 5 DE VIDEOJUEGOS")
print(videojuegos)

# Mostrar el primero y el ultimo
print(f"\nMi favorito (posicion 0): {videojuegos[0]}")
print(f"El de la posicion 5 (ultimo): {videojuegos[-1]}")

#Cambiar mi juego favorito
print("\n Cambio de opinión...")
videojuegos[0] = "Apex Legends"

print("Top 5 actualizado:")
print(videojuegos)


print("\nEjercicio6\n")
series = ["Stranger Things", "Wednesday", "The Last of Us"]

print("Series para ver:", series)

# Agregar una nueva serie
series.append("One Piece")
print('Agregaste One Piece:', series)

# Verificar si una serie está en la lista
if "Wednesday" in series:
    print("Ya tienes Wednesday en tu lista.")

if "Breaking Bad" not in series:
    print("Tienes Breaking Bad")
else:
    print("No tienes Breaking Bad en tu lista.")

# Ya viste la primera serie, la eliminas
print(f"\nYa terminaste de ver {series[0]}!")
series.pop(0)
print("Series restantes por ver:", series)

