# Escribe tu funcion aqui
def puedo_comprar(dinero_que_tengo, precio_producto):
    if dinero_que_tengo >= precio_producto:
       return " si puedes comprarlo"
    else: 
        return "no te alcanza"

# Pruebala con diferentes casos
resultado1 = puedo_comprar(500, 300) # Tengo 500 cuesta 300
print(f"Tenis nuevos: {resultado1}")

resultado2 = puedo_comprar(150,800) # Tengo 150 cuesta 800
print(f"Celular nuevo:{resultado2}")

resultado3 = puedo_comprar(1000, 100) # Tengo 100 cuesta 100
print(f"Audifonos: {resultado3}")


