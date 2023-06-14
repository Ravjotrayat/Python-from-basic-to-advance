#Seperate them,+ve and -ve number

l=[10,1.5,-5,-9,2,3,-4,7]
i=0
for j in range(len(l)):
    if l[j]<0:
        l[i],l[j]=l[j],l[i]
        i+=1
print(l)
