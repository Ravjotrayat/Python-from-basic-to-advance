'''
Question 6
For a given list of numbers find the its factors and add the factors
then if the sum of all factor is present in original list, sort it
and print it
Ex:
Input: 0,1,6
Factors: 0 = 0, sum =0
1 = 1, sum =1
6 =1,2,3 = sum =6
Output: 1,6
If the sum is not present in the list then return -1.
'''
def factor(l):
    final=[]
    for i in l:
        fac=[]
        for j in range(1,i):
            if i%j==0:
                fac.append(j)
        if sum(fac)==i:
            final.append(i)
    if final=='null':
        return -1
    else:
        return final
l=[0,1,6,36,7,8,9,10,21,22,23,24,25,26,27,28,29,30]
print(factor(l))
