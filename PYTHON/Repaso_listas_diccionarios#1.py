#Ejercicio_1
marcas_autos_chile = [
    "Toyota",
    "Hyundai",
    "Chevrolet",
    "Kia",
    "Nissan",
    "Ford",
    "Suzuki",
    "Mitsubishi",
    "Mazda",
    "Renault",
]
for marca in marcas_autos_chile:
    print(marca)
#Ejercicio_2
elemento = marcas_autos_chile.index("Kia")
print(elemento)
#Ejercicio_3
Eliminar = marcas_autos_chile.index("Kia")
marcas_autos_chile[Eliminar] = "Mercedes"
for marca in marcas_autos_chile:
    print(marca)
#Ejercicio_4
def get_position(marcas_autos_chile, elemento1):
    return marcas_autos_chile.index(elemento1)

#def reemplazar (marcas_autos_chile, elemento1, elemento2):
    #position = get_position(marcas_autos_chile, elemento1)
    #print(position)
    #marcas_autos_chile(position)= elemento1
    #return list

#reemplazar(marcas_autos_chile, "BMW", "Kia")
#Ejercicio_4
japon = [
    "Toyota"
    "Nissan"
    "Ford"
    "Susuki"
    "Misubishi"
    "Mazda"
    "Renault"
]
