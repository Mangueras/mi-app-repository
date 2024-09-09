#Ejercicio Cadenas Nº 1
print ("Ingresa una palabra para ver su cantidad de letras")
Frase = input()
print(len(Frase.replace (" ", "")))
#Ejercicio Cadenas Nº 2
print("Ingresa algun texto")
frase = input()
letra = input("Ingresa la letra que quieres ver cuantas veces se repite = ")
repeticiones = frase.count(letra)
print(f"Se repite {repeticiones} veces la letra")
#Ejercicio Cadenas Nº 3
frase = input()
print(len(frase.split()))
#Ejercicio Cadenas Nº 4
frase = input()
print(frase[::-1])
#Ejercicio Cadenas Nº 5
frase = input()
print(frase == frase[::-1])
#Ejercicio Cadenas Nº 6
frase = input()
subfrase = input()
print(frase.count(subfrase))
#Ejercicio Cadenas Nº 7
frase1 = ("hola no quiero comer porque no soy bueno comiendo")
frase2 = "no"
print (frase1.replace(frase2, "shi"))
#Ejercicio Cadenas Nº 8
