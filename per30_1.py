lista=[5,10,15,18,21]
i=0
while (lista[i]<18) and (i<len(lista)): #5\n10\n15  dove \n vuol dire "a capo"
    print(lista[i])
    i+=1
s="1234"
print("{}:{}".format(s[0],s[-2]))   # 1:3
