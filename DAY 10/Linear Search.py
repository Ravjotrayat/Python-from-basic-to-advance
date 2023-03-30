#Linear Search in Python

def linearsearch(array,n,x):
    for i in range(0,n):
        if array[i]==x:
            return i
    return -1

array=[1,2,53,5,3,5,36,4,354,5,4]
x=36
n=len(array)
result=linearsearch(array,n,x)
if result==-1:
    print("Element not found")
else:
    print("Element is present in the array at",result)
