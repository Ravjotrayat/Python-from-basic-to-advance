'''
Merge the 2 List.1st from starting and 2nd list from ending forming a word.
Input:
l1=['A','app','a','d','ke','th','doc','awa']
l2=['y','tor','e','eps','ay',None,'le','n']

Output : An apple a day keeps the doctor away
'''
l1=['A','app','a','d','ke','th','doc','awa']
l2=['y','tor','e','eps','ay',None,'le','n']
s=""
l2.reverse()
for i in range(0,len(l1)):
    if l1[i]==None:
        s+=l2[i]+" "
    elif l2[i]==None:
        s+=l1[i]+" "
    else:
        s+=l1[i]+l2[i]+" "      
print(s)
