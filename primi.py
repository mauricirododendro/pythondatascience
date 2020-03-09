def verificaPrimo(val):
    div=2
    while div< val:
        if val % div == 0:
            return False
        div=div+1
    return True
n=int(input("Quale n? "))  # se n vale 10 allora seguono gli output:2
                          #                                        3
                          #                                        5
                          #                                        7
num=2
while num<=n:
   ris=verificaPrimo(num)
   if ris==True:
      print(num)
   num=num+1
     
      
      
