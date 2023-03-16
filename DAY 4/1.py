#Find the nearest palindrome which accepts a number and returns
# the nearest palindrome greater than the given number.
#Input=> 99,1221
#Output=> 101,1331
'''
def nearest_palindrome(num):
    d=0
    a=num
    while num>0:
        d=(d*10)+num%10
        num//=10
    if d==a:
        return True
    else:
        return False
num=int(input())
num+=1
while True:
    if nearest_palindrome(num):
        print(num)
        break
    num+=1 
        '''
# Other way of doing is.....
def nearest_palindrome(num):
    if str(num)==str(num)[::-1]:
        return True
    else:
        return False
num=int(input())
num+=1
while True:
    if nearest_palindrome(num):
        print(num)
        break
    num+=1   

