#ewQuestion 1
'''
Write a python lambda expression for calculating simple interest.
If simple interest is greater than 1000, display as “Platinum Member”,
otherwise “Gold Member”.
Use the below formula to calculate the simple interest.
S_interest=(principal_amount*duration in years*rate_of_interest)/100
'''

a=int(input("Enter the Principal amount\n"))
b=int(input("Enter the Time Period\n"))
c=int(input("Enter the rate of interest\n"))
x=lambda a,b,c:a*b*c*0.01
if x(a,b,c)>1000:
    print("Platinum Member")
else:
    print("Gold Member")
