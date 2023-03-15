#Find the largest Prime Factor
#input=f(10)+f(11)+f(12)+f(13)+f(14)+f(15)+f(16)+f(17)+f(18)
#output=5+11+3+13+7+5+2+17+3= 66

import math
def prime(j):
    for k in range(2,int(math.sqrt(j))+1):
        if j%k==0:
            return 0  
    return j    
    
def prime_list(ls):
    m=0
    for j in ls:
        d=prime(j)
        if d!=0:
            m=max(m,d)
    return m

def Summ(i):
    ls=[]
    for j in range(1,i+1):
        if i%j==0:
            ls.append(j)
    return prime_list(ls)

n=int(input())  
su=0
for i in range(n,n+9):
    su=su+Summ(i)
print("Sum",su)
