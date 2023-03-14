"""
#List,tuple and dicrionary

#List => ordered data structure,default indexing,mutable,diff. data types,
lis = [10,10,"Ravjot",True]
lis.append(564)
print(lis)
lis.extend([3,5434,56,6])
print(lis)
lis.insert(2,56000)
print(lis)
lis.remove(56000)
print(lis)
lis.pop()    #by default last number will be removed
print(lis)
lis.pop(1)
print(lis)
del lis[5]
print(lis)

"""

#Accept a sentence return no. letters of words and numbers
#  input  Infosys  123   output  :  [7,3]
#isdigit()=>numbers , isalpha()=>letters
'''
sen=input()
n,c=0,0
lis=[]
for i in sen:
    if i==" " :
        continue
    elif i.isnumeric() :
        n=n+1
    else:
        c=c+1
lis.extend([c,n])  
print(lis)

#Ma'am's solutions
for i in sem:
    if i.isalpha():
        n++
    elif i.isdigit():
        c++
    else:
        continue:

'''
'''
#find pairs of numbers accept a list of positive integers with no repitations
# and return count of pais
#input:[1,2,7,4,5,6,0,3] and 6    output:3

def pairs_of_numbers(ls,a):
    c=0
    for i in range(0,len(ls)):
        for j in range(i+1,len(ls)):
            if ls[i]+ls[j]==a:
                c=c+1

    return(c)
ls=[3,4,1,8,5,9,0,6]
a=9
result=pairs_of_numbers(ls,a)
print(result)

'''

"""
#first and last 2
def slicing(ss):
    if len(ss)<2:
        return -1
    else:
        result=ss[0:2]+ss[-2:]
        return result
s=input()
result=slicing(s)
print(result)
"""

'''
#Add lg after ing and no ing the add ly
def ingly(a):
    if len(a)<3:
        return a
    else:
        a.lower()
        if s[-3:]!='ing':
            a=a+"ing"
        else:
            a=a+"ly"
    return a
s=input()
print(ingly(s))
'''

'''
# example input 125874,output 251748
def check_double(n):
    num=2*n
    ls=[]
    if len(str(n))!=len(str(num)):
        return False
    while n>0:
        ls.append(n%10)
        n=n//10
    while num>0:
        d=num%10
        if d in ls:
            i=ls.index(d)
            ls.pop(i)
        else:
            return False
        num=num//10
    return True
num=int(input())
print("Result = ",check_double(num))



no = int(input())
double = no*2;
num = str(no)
num2 = str(double)
flag = "true"
if len(num) == len(num2):
    for i in num:
        if  i in num2:
            continue
        else:
            flag = "false"              
print(flag)

'''
"""
def find_more_than_average(a):
    avg=sum(a)//len(a)
    c=0
    for i in a:
        if i>=avg:
            c=c+1
    return c*10

def generate_frequency(a):
    ls=[]
    for i in range(0,26):
        c=0
        for j in range(0,len(a)-1):
            if i==a[j]:
                c=c+1
        ls.append(c)
    return ls
def sort_marks(a):
    a=sorted(a)
    return a

a=(12,18,25,24,2,5,18,20,20,21)
print("Average ",find_more_than_average(a))
print("Frequency ",generate_frequency(a))
print("Marks ",sort_marks(a))    

"""

"""
#dictionary using
def translate(a,b):
    ls=[]
    for i in b:
        ls.append(a[i])
    return ls
a={"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
b=["merry","christmas"]
print("Translated meaning is: ",translate(a,b))
"""

#number of distint subarray in an array of position integer such that the sum of
# subarray is an odd integer,2 subarrays are considered diff. if they start or end
# at diff index input
a=int(input())
b=int(input())
array=[i for i in range(a,b+1)]
result=[]
ls=[]
#for i in range(len(array)):
 #   for j in range(i,len(array)):
  #      result.append(array[i,j+1])

ls=[result[i:j+1]  for i in range(len(array)) for j in range(i,len(array))]
print(ls)
















    
