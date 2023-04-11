def fun(a,b):
    if (a & b)>0:
        return 1+fun(a-1,b)+fun(a,b-1)
    return 0
print(fun(2,2))
