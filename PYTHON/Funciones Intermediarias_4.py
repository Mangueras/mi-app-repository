costa_rica = {
   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

def imprimirInformacion(diccionario):
    for llave, lista in diccionario.items():
        print(f"len({len(lista)}) {llave.upper()}")
        for item in lista:
            print(item)
        print()

imprimirInformacion(costa_rica)
