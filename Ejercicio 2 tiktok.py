# Escribe tu funcion aqui
def calcular_horas_tiktok(minutos_por_dia):
    minutos_totales = minutos_por_dia * 7
    horas_totales = minutos_totales / 60
    return horas_totales

# Pruebala con diferentes valores 
horas = calcular_horas_tiktok(30) # 30 minutos por dia
print(f"Ves {horas} horas de tiktok a la semana")

horas2 = calcular_horas_tiktok(60) # 60 minutos por dia
print(f"Ves {horas2} horas de tiktok a la semana")
