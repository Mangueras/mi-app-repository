#Ejercicio_1
cantantes = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"},
   {"nombre": "José José", "pais": "México"},
   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]
def iterar_diccionario(lista):
    for diccionario in lista:
        for llave, valor in diccionario.items():
            print(f"{llave}  {valor}")

iterar_diccionario(cantantes)