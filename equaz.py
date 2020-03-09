print('inserisci i coefficienti')
a=int(input('a?'))
b=int(input('b?'))
c=int(input('c?'))
delta=b**2-4*a*c
if delta>0:
    rad=delta**0.5
    x1=float(-b-rad)/(2*a)
    x2=float(-b+rad)/(2*a)
else:
    rad=(-delta)**0.5
    x1="(-%f -%fi)/(2*%f)" % (b,rad,a)
    x2="(-%f +%fi)/(2*%f)" % (b,rad,a)
print(x1,x2)    
    
