def funn(a,b):
    if b%a<2:
        b=b>>1
        print("I am A",b)
        return a
    
    if a%b<2:
        b=b+12
        print("I am B",b)
        return b
    print("No one")
    return a+b+5

print(funn(3,9))
