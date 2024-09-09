#Ejercicio Nº1
for i in range(101):
    print([i])
#Ejercicio Nº2
for i in range(501):
    if i% 2 == 0:
        print([i])
#Ejercicio Nº3
for i in range (1,101):
    if i% 5 == 0:
        print("Ice Ice")
    else:
        i% 10 == 0
        print("Baby")
#Ejercicio Nº4
sum=0
for i in range (0, 500001):
    if i%2 == 0: 
        sum +=i
print(sum)
#Ejercicio Nº5
for i in range(2024,0,-3):
    print(i)
#Ejercicio Nº6
numinicial = 3
numfinal = 10
nummultiplo = 2
for i in range(numinicial,numfinal+1):
    if i%nummultiplo == 0:
        print(i)