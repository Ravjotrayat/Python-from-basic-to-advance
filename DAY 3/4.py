#Example:input with comma
#input => 3,2,6,5,1,4,8,9
#         num1=3+2+6+9=20 excluding[from 5 -> 8],
#         num2=5148(from 5 to 8 in string form),
#Output=> 5148+20=5168

array=list(map(int,input().split(',') ))
num=sum(array[:array.index(5)])+sum(array[array.index(8)+1:])
l=array[array.index(5):array.index(8)+1]
no=""
for i in l:
    no+=str(i)
print(int(num)+int(no))
