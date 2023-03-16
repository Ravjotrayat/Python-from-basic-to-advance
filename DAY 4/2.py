
'''
n=int(input())
for i in range(n):
    id=int(input())
    special=input()
    dic[id]=special
    '''
#dic=[101,'P',102,'O',302,'P',305,'P']
#dic=[101,'O',102,'O',302,'P',305,'E',402,'O',656,'O']
#dic=[101,'O',102,'E',302,'P',305,'P',401,'E',656,'O',987,'E']
d={"P":"Pediatrics","O":"Orthopedics","E":"Ent"}
p=dic.count('P')
e=dic.count('O')
o=dic.count('E')
if p>e and p>o:
    speciality=d['P']
elif e>p and e>o:
    speciality=d['E']
else:
    speciality=d['O']
print(speciality)

