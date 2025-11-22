print("Ejercicio 1\n")

canciones_dia = ("blinding Lights", "Heat waves", " Anti- hero")
canciones_noche = ("Leaviting", "As it was")
playlist_completa = canciones_dia + canciones_noche
print(canciones_dia) 
print(canciones_noche)
print(playlist_completa)


print("\nEjercicio 2\n")
ubicaciones_norte = ((19.5, -99.2), (19.6, -99.3))
ubicaciones_sur = ((19.4, -99.1), (19.3, -99.4))

todas_ubicaciones = ubicaciones_norte + ubicaciones_sur
print(ubicaciones_norte)
print(ubicaciones_sur)
print(todas_ubicaciones)

print("\nEjercicio3 - Repeticion\n")

emojis = ("❤️", "😍")
cartel = emojis * 5
print(emojis)
print(cartel, "\n")

print("\nEjercicio4 - Longitud\n")

seguidores_tiktok = 1500
seguidores_insta = 2300
seguidores_fb = 950
seguidores_total = seguidores_tiktok + seguidores_insta + seguidores_fb
seguidores = (seguidores_tiktok, seguidores_insta, seguidores_fb)
cantidad_redes = len(seguidores)

print("seguidores en tiktok:", seguidores_tiktok)
print("seguidores en instagram:", seguidores_insta)
print("seguidores en facebook", seguidores_fb)
print("total de seguidores:", seguidores_total)
print("cantidad de redes sociales:", cantidad_redes)

print("\nEjercicio5 - count\n")

resultados_partidas = ("gane", "perdi", "gane", "gane", "perdi", "gane", "empate")
veces_gane = resultados_partidas.count("gane")


print("\nEjercicio 6 - index\n")

ranking = ("marcelo", "mariana", "vane", "abi", "fer", "marcelo", "orlando")
mi_posicion = ranking.index("mariana")
print("estoy en la posicion:", mi_posicion, "\n")

print("\nEjercicio 7 - Slicing\n")

juegos = ("Minecraft", "Fortnite", "Roblox", "Among Us", "Valorant", "GTA V", "ACIH", "Call of Duty")
ultimos_tres = juegos[2:5]
print(ultimos_tres)


print("\nEjercicio 8 - Recorrer tupla\n")

canciones = ("EYES CLOSED", "The Fate of Ophelia", "When Did You Get Hot?", "Golden")

for cancion in canciones:
    print(cancion)

print("\nEjercicio 9 - Verificar si un elemento existe\n")

grupo_proyecto = ("Meli", "Alex", "Mia", "Andrea")

print("Integrantes del grupo:", grupo_proyecto)
print("\n¿Mia está en el grupo?")
print("Mia" in grupo_proyecto)

print("\n¿Orlando está en el grupo?")
print("Orlando" in grupo_proyecto)

print("\nEjercicio 10 - Ordenar la tupla\n")

puntuaciones = (580, 250, 1040, 390, 750, 2480, 870, 138, 938)

puntuaciones_ordenadas = tuple(sorted(puntuaciones))

print(puntuaciones_ordenadas)