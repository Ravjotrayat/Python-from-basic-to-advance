n=["good","bad","goo","bad","good"]
new={}
for i in n:
    if i in new:
        new[i]+=1
    else:
        new[i]=1
maxx=0
word=""
for i,j in new.items():
    if j>maxx:
        maxx=j
        word=i
        
    elif maxx==j:
        if len(word) < len(i):
            maxx=word
print(word,"=>",maxx)            
         
            
    
    

