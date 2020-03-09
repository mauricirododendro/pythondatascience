l=[1,2,3,4,5]
print(l[0])      #1
l.append(l[0]+l[4])
print (l)        # [1,2,3,4,5,6]
m=l[2:5]
print (m)        #[3,4,5]
m.pop(2)
print (m)        #[3,4]
print(sorted(l,reverse=True))    #[6,5,4,3,2,1]
print(l)                         #[1,2,3,4,5,6]
