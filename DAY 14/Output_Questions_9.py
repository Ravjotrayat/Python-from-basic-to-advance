def large(n):
    if n<=1:
        return 1
    if n%4==0:
        return large(n/4)
    if large(n/4)+large(n/4*1):
        return large()
    
print(large(64))
