#categories of function
#based on arguments
#(data is sent from right to left)==
#1:Positional arguments = not given all 4 parameter,only provided 3 0r 5,so positional argument required
def functional(a,b,c,d):
    print("N1",a,"N2",b,"N3",c,"N4",d*a)
functional(10,20,230,"39")

#2:Keywords arguments
def functional(a,b,c,d):
    print("N1",a,"N2",b,"N3",c,"N4",d)
functional(b=10,a=20,d=230,c=39)
print()
#3:Default arguments
def functional2(aa,bb,cc="paji",dd="GIET"):    # Default value hase to be right most corner
    print(aa,bb,cc,dd)
functional2("Ravjot",167)
functional2("Ayush",147)
functional2("Abhilash",182,"Lord_VENU")
functional2("Raman",00,"Singh")

print()
def functional3(*var):
    sum=0
    for i in var:
        sum+=i
    return(sum)
print(functional3(10,100,200))
print()
print(functional3(34,43,87,22))
print()
print(functional3(12,20))
