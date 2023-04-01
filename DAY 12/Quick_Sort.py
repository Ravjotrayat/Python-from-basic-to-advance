def partition(array,low,high):
    pivot=array[high]
    i=low-1
    for j in range(low,high):
        if array[j]<=pivot:
            i=i+1
            array[i],array[j]=array[j],array[i]
    array[i+1],array[high]=array[high],array[i+1]
    return i+1

def Quicksort(array,low,high):        
        if low<high:
            pi=partition(array,low,high)
            Quicksort(array,low,pi-1)
            Quicksort(array,pi+1,high)

array=[8,7,6,1,0,9,2]
print(array)
Quicksort(array,0,len(array)-1)
print(array)
