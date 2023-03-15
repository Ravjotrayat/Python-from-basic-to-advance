#Input 5 sentences and remove the words of stop list provided.
#Output => [['new', 'world', 'record', 'set'],
#           ['holy', 'city', 'ayodhya'],
#           ['eve', 'diwali', 'tuesday'],
#           ['over', 'three', 'lakhs', 'diya', 'or', 'earthen', 'lamps'],
#           ['lit', 'up', 'simultaneouly', 'banks', 'saraya', 'river']]
sen=["a new world record was set"
     ,"in the holy city of ayodhya",
     "on the eve of diwali on tuesday",
     "with over three lakhs diya or earthen lamps",
     "lit up simultaneouly on the banks of the saraya river"
     ]

stop=['for','a','of','the','and','to','in','on','with','was']
c=0
print([
           [ j for j in i.split(' ')
                 if j not in stop
           ]
    for i  in sen    
    ])
