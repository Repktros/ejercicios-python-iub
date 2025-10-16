num_lista = list(range (1,101))

for numero in num_lista:
    if numero % 5 == 0:
        print (numero)

 # O, alternativa
 
for numero2 in range(1,101):
    if numero2 % 5 == 0:
        print ("Alternativa: ",numero2)