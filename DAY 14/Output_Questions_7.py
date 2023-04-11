def foo(n):
    if n==1:
        return 1
    elif n%2==0:
        return 2*n
    else:
        return foo( n - 3)
n=25
print(foo(n))
#Output=44
