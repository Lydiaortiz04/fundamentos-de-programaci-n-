print("Ejercicios diccionarios - martes \n")
print("\nEjercicio 1\n")
# Escribe tus datos
usuario = {
    "nombre": "Lydia",
    "edad": 18,
    "ciudad": "Monterrey"
}
print("Diccionario completo:")
print(usuario)
print("\nAcceso a valores individuales:")
print("Nombre:", usuario["nombre"])
print("Edad:", usuario["edad"])
print("Ciudad:", usuario["ciudad"])


print("\nEjercicio 2\n")
videojuego = {
    "titulo": "minecraft",
    "plataforma": "pc",
}
print("Diccionario original:")
print(videojuego)
videojuego["año"] = 2019
videojuego["genero"] = "sandbox"
videojuego["es_multijugador"] = True

print("\nDiccionario despues de agregar datos:")
print(videojuego)
print("\nNuevos datos agregados")
print("Año:", videojuego["año"])
print("Género:", videojuego["genero"])
print("Es multijugador:", videojuego["es_multijugador"])


print("\nEjercicio 3\n")
perfil = {
    "usuario": "Lydia",
    "seguidores": 750,
    "publicaciones": 4,
    "ciudad": "Monterrey"
}
print("Perfil original:")
print(perfil)
perfil["seguidores antes:"] = perfil["seguidores"] 
perfil["seguidores"] = 1500
perfil["publicaciones"] = 45
print("\nPerfil despues de actualizar datos:")
print(perfil)
print("seguidores ahora:", perfil["seguidores"])
print("publicaciones ahora:", perfil["publicaciones"])


print("\nEjercicio 4 - eliminar un par clave-valor\n")
cuenta = {
    "usuario": "Lydia",
    "email": "lydiaortiz1405@gmail.com",
    "telefono:": "8341333731",
    "ciudad": "Monterrey"
}
print("Cuenta original(con telefono):")
print(cuenta)
del cuenta["telefono:"]
print("\nCuenta despues de eliminar el telefono:")
print(cuenta)
print("\nVerificacion - existe 'telefono'?:", "telefono:" in cuenta)


print("\nEjercicio 5 - len\n")
pelicula = {
    "titulo": "after",
    "director": "Jenny Gage",
    "año": 2019,
    "genero": "romance adolescente",
    "duracion_minutos": 105,
    "calificacion": 7.0
}
print("Película:")
print(pelicula)
cantidad = len(pelicula)
print("\n Cuantos datos tiene el diccionario?:", cantidad)
print("El diccionario tiene", cantidad, "pares clave-valor.")


print("\nEjercicio 6 - obtener los keys\n")
cancion = {
    "titulo": "Heart of gold",
    "artista": "Shawn Mendes",
    "album": "Shawn",
    "año": 2024,
    "genero": "pop",
    "duracion_segundos": 170
}
print(" Diccionario de canción:")
print(cancion)
print("\n Todas las claves o datos del diccionario:")
claves = cancion.keys()
print(claves)

print("\nMostrandon claves una por una:")
for clave in claves:
    print("-", clave)

print("Ejercicio 7 - obtener los values")
calificaciones = {
    "economia": 9.7,
    "derecho de aduanas": 8.5,
    "admin de negocios": 9.0,
    "Logistica y cadena de suministro": 8.8,
    "mercadotecnia internacional": 9.2
}
print("Diccionario de calificaciones:")
print(calificaciones)
print("\n Todos los valores del diccionario:")
valores = calificaciones.values()
print(valores)