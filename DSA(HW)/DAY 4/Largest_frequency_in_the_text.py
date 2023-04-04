'''
Write a python program that accepts a text and displays a 
string which contains the word with the largest frequency
 in the text and the 
frequency itself separated by a space.
Rules:
The word should have the largest frequency.
In case multiple words have the same frequency, then choose 
the word that has the maximum length.
Assumptions:
The text has no special characters other than space.
The text would begin with a word and there will be only a 
single space between the words.
Perform case insensitive string comparisons wherever 
necessary.

'''

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
         
            
    
    

