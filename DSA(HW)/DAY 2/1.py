#Comparment in simple list
class Compartment:
    def __init__(self,name,total_seating,num_passenger):
        self.name=name
        self.total_seating=total_seating
        self.num_passenger=num_passenger

class Train:
    
    def __init__(self,train_name,compartment_list):
        self.train_name=train_name
        self.compartment_list=compartment_list

    def get_train_name(self):
        return self.train_name

    def get_compartment_list(self):
        return self.compartment_list
        
    def count_compartments(self):   #return the total no of compartment
        return len(self.compartment_list)


#returns the count of the compartment in which more than 50% of seats
        #are vacant
        
    def check_vacancy(self):
        count=0
        for compartment in self.compartment_list:
            if compartment.num_passenger<compartment.total_seating*0.5:
                count+=1
        return count

compartment1=Compartment("SL",250,400)
compartment2=Compartment("2AC",125,280)
compartment3=Compartment("3AC",120,300)
compartment4=Compartment("FC",160,300)
compartment5=Compartment("1AC",100,210)

train=Train("Rajdhani Express",[compartment1,compartment2,compartment3,compartment4,compartment5])

print(train.get_train_name())  
print(train.count_compartments())
print(train.check_vacancy())

