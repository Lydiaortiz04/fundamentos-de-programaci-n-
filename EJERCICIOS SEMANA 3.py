# Ejercicio 1 
# SALIDA - Bienvenida
print ("="*45)
print(" BIENVENIDO A GAME STORE ")
print ("="*45)
print ()

# ENTRADA - Datos del cliente
nombre = input("Ingrese su nombre:")
edad = int(input("Ingrese su edad:"))
# PROCESAMIENTO - Precios fijos de los juegos
precio_fifa = 899.00
precio_cod = 1299.00
precio_hello_kitty = 599.00

# SALIDA - Catalogo de productos
print("------- CATALOGO DE PRODUCTOS -------")
print("1. FIFA 2025 - $" + str(precio_fifa))
print("2. Call of Duty - $" + str(precio_cod))
print("3. Hello Kitty Island Adventure - $" + str(precio_hello_kitty))
print()

# ENTRADA - cantidad de cada juego
cantidad_fifa = float (input(" cuantos FIFA 2025 quieres? "))
cantidad_cod = float (input(" cuantos Call Of Dutty quieres? "))
cantidad_hello_kitty = float (input(" cuantos Hello Kitty Island Adventure quieres? "))

# PROCESAMIENTO - Calculos por juego
total_fifa = precio_fifa * cantidad_fifa
total_cod = precio_cod * cantidad_cod
total_hello_kitty = precio_hello_kitty * cantidad_hello_kitty

# PROCESAMIENTO - Calculos totales 
subtotal = total_fifa + total_cod + total_hello_kitty
iva = subtotal * 0.16
total = subtotal + iva

# PRICESAMIENTO - Cantidad total de juegos
cantidad_total_juegos = cantidad_fifa + cantidad_cod + cantidad_hello_kitty

# PROCESAMIENTO - Crear ticket
print("TICKET DE COMPRA")
print("="*45)
print("Cliente: " + nombre)
print("Edad: " + str(edad) + " años")
print("-"*45)
print("DETALLE DE COMPRA:")
print("FIFA2025:")
print(" Cantidad: " + str(cantidad_fifa))
print(" Precio unitario: $" + str(precio_fifa))
print(" Total: $" + str(total_fifa))
print("Call of Duty:")
print(" Cantidad: " + str(cantidad_cod))
print(" Precio unitario: $" + str(precio_cod))
print(" Total: $" + str(total_cod))
print("Hello Kitty Island Adventure:")
print(" Cantidad: " + str(cantidad_hello_kitty))
print(" Precio unitario: $" + str(precio_hello_kitty))
print(" Total: $" + str(total_hello_kitty))
print("-"*45)
print("Cantidad total de juegos: " + str(cantidad_total_juegos))
print("Subtotal: $" + str(subtotal))
print("IVA (16%): $" + str(iva))
print("="*45)
print("TOTAL A PAGAR: $" + str(total))
print ()
# SALIDA - Mensaje de despedida
print("Gracias por su compra, " + nombre + ". ¡Vuelva pronto!")



# EJEMPLO 1 - CONTROL DE ACCCESO A VIDEOJUEGOS
print("="*22)
print("Ejercicio 1\n")

edad = int(16)

if edad >= 16:
    print("Acceso permitido a todos los videojuegos.")
else:
    print("Acceso restringido a videojuegos para adultos.")


# EJEMPLO 2 - CALCULADORA DE PROMEDIO ESCOLAR
print("Ejercicio 2 con AND\n")

calificacion = int(input("Ingrese su calificación (0-100): "))

if calificacion >= 90 and calificacion <= 100:
    print("Excelente")
elif calificacion >= 80 and calificacion < 90:
    print("Aprobado")
elif calificacion >= 60 and calificacion < -70:
    print("No aprobado")
else:
    print("calificación inválida")



    #EJEMPLO 3 - SISTEMA DE RECOMENDACION DE PELICULAS
print("="*13)
print("Ejercicio 3\n")

edad = int(input("Ingrese su edad: "))
if edad < 13:
    print("Te recomendamos peliculas infantiles.")

elif edad >= 13 and edad <= 17:
    genero = input(" cual es tu genero favorito (accion, comedia, terror): ").lower ()

    if genero == "accion":
        print("Te recomendamos Spider-man (PG-13).")
    elif genero == "comedia":
        print("Te recomendamos Shrek (PG-13).")
    elif genero == "terror":
        print("Te recomendamos Scary Stories (PG-13).")

elif edad >= 18:
    genero = input(" cual es tu genero favorito (accion, comedia, terror): ").lower ()

    if genero == "accion":
        print("Te recomendamos John Wick.")
    elif genero == "comedia":
        print("Te recomendamos The Hangover.")
    elif genero == "terror":
        print("Te recomendamos The Conjuring.")
        

