lista=[1,2,3,4,5,6,7,8]
for i in range(0,7,2):    #data una lista di 8 elementi scambiare un elemento
                          #con il suo successivo
    print(i)
    lista[i],lista[i+1]=lista[i+1],lista[i]
print (lista)    
