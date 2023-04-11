def fun(a,b):
    if a&1 and 1:
        return fun(a-1,a+a)+fun(a-1,b+b)
    else:
        return b^a
print(fun(1,3))
        
