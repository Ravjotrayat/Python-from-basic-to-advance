#python programming

#data types
name="ravjot"   #interperter,object,runtime
print("Name",name,type(name))
roll = 167  #
print("roll",roll,type(roll))
per=88.8
print("Percentage",per,type(per))
complex_number=3+4+5j
print("complex_number",complex_number,type(complex_number))

#decision  making commands
#Program : multiple of 3
a=int(input("Enter the number\n"))
if a%3==0 and a%5==0:
    print("Multiple of 3 and 5")
elif a%3==0:
    print("Multiple of 3")
elif a%5==0:
    print("Multiple of 5")
else:
    print("Invalid")

#Print from 1 to 100
for i in range(0,100):
    print(i+1,end=' ')
print()

#Print odd numbers from 0 to 100
for i in range(0,99,2):
    print(i+1,end=' ')
print()

#Print even numbers from 0 to 100
for i in range(1,100,2):
    print(i+1,end=' ')
print()
 
#Print from 100 to 1
for i in range(100,0,-1):
    print(i,end=' ')
print()


#Print odd numbers in reverse from 100 to 0
for i in range(99,0,-2):
    print(i,end=' ')
print()


#even numbers in reverse from 100 to 1 
for i in range(100,1,-2):
    print(i,end=' ')
print()















