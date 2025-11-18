print("\nEjempplo 1 mostrar el menu\n")

def mostrar_menu():
    print("=== MENU ===")
    print("1. Hamburguesa")
    print("2. pizza")
    print("3. tacos")

# La usas asi y ya no tienes que escribir todo el menu
mostrar_menu()


print("\nEjemplo2 la fav cancion\n")

def reproducir_favorita():
    print(" reproduciendo: 'Blinding lights' de the weeknd")

# la usas asi:
reproducir_favorita()


print("\nEjemplo 3 reglas del juego\n")
def mostrar_reglas():
    print("REGLAS DEL JUEGO:")
    print("- No hacer trampa")
    print("- Respetar turnos")
    print("- Divertirse")

# La usas asi
mostrar_reglas()


# FUNCIONES CON PARAMETROS
print("\nEjemplo 4\n")

def reproducir_cancion(nombre_cancion):
    print(f" Reproduciendo: {nombre_cancion}")

# La usas asi (cada vez es DIFERENTE):
reproducir_cancion("Bad Bunny - Titi me pregunto")
reproducir_cancion("Karol G - TQG")
reproducir_cancion("Taylor swift - Anti-Hero")


def calcular_impuesto(precio):
    total= precio * 1.16 #16%
    return total

# La usas asi (cada precio es DIFERENTE):
print(calcular_impuesto(110))
print(calcular_impuesto(500))
print(calcular_impuesto(1200))


