# Taking an input as string:integer and if sum of the squares of the numbers
# is even,then rotate 1 to left otherwise rotate 2 to right .

#input => rhdt:246
#         ghftd:1246

#Output =>trhd
#         ftdgh

dic=input().split(':')
a=int(dic[1])
s=0
first=dic[0]
st=""
while a>0:
    s+=(a%10)**2
    a=a//10
if s%2==0:
    st=first[-1]+first[:len(first)-1]
else:
    st=first[2:]+first[0:2]
print(st)
        
# taken 2 or more inputs together separated by " , "
#input => rhdt:246,ghftd:1246

def splitting(i):
    dic=i.split(':')
    a=int(dic[1])
    first=dic[0]
    su=0
    st=""
    while a>0:
        su+=(a%10)**2
        a=a//10
    if su%2==0:
        st=first[-1]+first[:len(first)-1]
    else:
        st=first[2:]+first[0:2]
    return st
dic=input().split(',')
for i in dic:
    print(splitting(i))

#input => rhdt:246,ghftd:1246
