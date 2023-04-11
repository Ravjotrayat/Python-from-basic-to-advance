i=0
s=0
n=127
while n>0:
    r=n%10
    p=8^i
    s+=p*r
    i+=1
    n/=10

print(int(s))

#Output is: 84 (Calculate Manually)
#not 94 
