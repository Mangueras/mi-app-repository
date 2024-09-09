import math 

#Ejercició 1
num1 = 10
num2 = 2
suma = (num1+num2)
print("La suma es = " + str(suma))
#Ejercició 2
num1 = 10
num2 = 2
resta = (num1-num2)
print("La resta es = " + str(resta))
#Ejercició 3
num1 = 10
num2 = 2
multiplicación = (num1*num2)
print("La multiplicación es = " + str(multiplicación))
#Ejercició 4
num1 = 10
num2 = 2
división = (num1/num2)
print("La  es = " + str(división))

num3 = int(input("Ingrese un Numero "))
num4 = int(input("Ingrese un Numero "))
#Ejercició 1
suma = (num3+num4)
print("La suma es = " + str(suma))
#Ejercició 2
resta = (num3-num4)
print("La resta es = " + str(resta))
#Ejercició 3
multiplicación = (num3*num4)
print("La multiplicación es = " + str(multiplicación))
#Ejercició 4
división = (num3/num4)
print("La Divición es = " + str(división))
#Ejercició 5
num5 = int(input("Ingrese un Numero "))
num6 = int(input("Ingrese un Numero "))
Elevación = (num5**num6)
print("La Elevación es = " + str(Elevación))

#Ejercició 6
num7 = float(input("Ingrese Numero "))
Raíz = math.sqrt(num7)
print(f"La Raíz es = {Raíz} ")

#Ejercició 7
num8 = float(input("Ingrese Numero "))
Absoluto = abs(num8)
print(f"El Valor Absoluto es = {Absoluto} ")

#Ejercició 8
x = round(3.1415, 4)
print(x)

#Ejercició 9
num9 = int(input("Ingrese un Numero "))
num10 = int(input("Ingrese un Numero "))
maximo = max(num9, num10)
print("El número máximo es:", maximo)

#Ejercició 10
num11 = int(input("Ingrese un Numero "))
num12 = int(input("Ingrese un Numero "))
minimo = min(num9, num10)
print("El número minimo es:", minimo)

#Ejercició 11
base1 = int(input("Ingrese la base de su Triangulo"))
altura1 = int(input("Ingrese la altura de su Triangulo "))
calculo1 = (base1*altura1/2)
print("El Area de su Triangulo es:", calculo1)

#Ejercició 12
radio = int(input("Ingrese el radio de su Circulo "))
calculo2 = math.pi * radio **2
print("El Area de su Circulo es:", calculo2)