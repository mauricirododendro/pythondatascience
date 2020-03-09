segno=-1
somma=0.0
n=int(input('inserisci numero intero '))#si calcola somma di -1+1/2-1/3....
for i in range(1,n+1):
    #print(i)
    #j=float(1/i)
    #print(j)
    somma +=(1/i)*segno
    #print(somma)
    segno=segno*(-1)

print(somma)    
