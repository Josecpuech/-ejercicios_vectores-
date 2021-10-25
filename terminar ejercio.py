import random
lista=[0,0,0,0,0,0,0,0,0,0]
contador=0 
for i in range (1,15):
    lista [0]= random.randint(1,15)


for i in lista:
    if(i%2==0):
        contador=contador+1
    


print("los numeros pares que hay en la lista son:", contador )

print (lista)
