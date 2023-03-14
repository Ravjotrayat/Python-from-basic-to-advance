'''
a=int(input())
b=int(input())
c=int(input())
if a==7:
    print(b*c)
elif b==7:
    print(c)
elif c==7:
    print(-1)
else:
    print(a*b*c)

'''

'''

currency=input()
currency=currency.lower()
amount=int(input("Enter the amount"))
rupees=0.0
if currency == 'euro':
    rupees=amount*0.01417
    print(rupees)
elif currency == 'british pound':
    rupees=amount*0.0100
    print(rupees)
elif currency == 'australian dollar':
    rupees=amount*0.02140
    print(rupees)
elif currency=='canadian dollar':
    rupees=amount*0.02027
    print(rupees)
else :
    print(-1)

'''
'''
# output == 204910
amount=0.0
adult=int(input("Adults"))
child=int(input("Child"))
amount=0.90*(1.07*((37550.0*adult)+(child*37550.0)/3))
print(amount)

'''

a=int(input("1 Rupee coin "))
b=int(input("5 Rupee coin "))
c=int(input("Amount "))
if (a*1 + b*5 )<c:
    print(-1)
else:
    n=c%5
    m=c//5
    print("5 rupees coin",m)
    print("1 rupees coin",n)
   
    
    
    
    
        



    
