#Binary Search

def binarysearch(array,x,low,high):
    while low<=high:
        mid=low+(high-low)//2
        if array[mid]==x:
            return mid
        elif array[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1
                 
array=[4,6,7,8,9,10,12,13,15]
x=6
result = binarysearch(array,x,0,len(array)-1)
if result==-1:
    print("Number is not present")
else:
    print("Element is present at index=",str(result))
