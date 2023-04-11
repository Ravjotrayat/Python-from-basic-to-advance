def f1(n,r):
    if n>0:
        return (n - r + f1((n/3,13))
    else:
        return 0
n,r=39,13
print(f1(n,r))
# Output should be 5
