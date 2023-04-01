def SelectionSort(array,size):
    for i in range(size):
        kmin=i
        for j in range(i+1,size):
            if array[kmin]>array[j]:
                kmin=j
        array[i],array[kmin]=array[kmin],array[i]
array=[20,12,10,15,2]
size=len(array)
SelectionSort(array,size)
print(array)
