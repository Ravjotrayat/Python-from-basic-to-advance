# Check if numbers in list2 is present in list1 . Print number with position
# in tuple,dictionary and normal loop form using tuple.
#Input => [9,3,6,1,5,0,8,2,4,7]
#         [6,4,6,1,2,2]
#Output => [(6, 2), (4, 8), (6, 2), (1, 3), (2, 7), (2, 7)]
#          {6: 2, 4: 8, 1: 3, 2: 7}
#          [(6, 2), (4, 8), (6, 2), (1, 3), (2, 7), (2, 7)]

mylist=[9,3,6,1,5,0,8,2,4,7]
listb=[6,4,6,1,2,2]
#In tuple
print([(i,mylist.index(i))
       for i in listb 
        ])

#In Dictionary
print({i:mylist.index(i)
       for i in listb 
        })


#In for loop`
ls=[]
for i in listb:
    if i in mylist:
        tup=(i,mylist.index(i))
        ls.append(tup)
print(ls)
