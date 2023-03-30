Question:
'''A train is identified by its name and list of compartments.
The compartments are identified by its name,total seating 
capacity and the number of passengers.
Implement the class Train as given in the class diagram.
Train
- train_name
- compartment_list
_init_(train_name,compartment_list)
+ get_train_name()
+ get_compartment_list()
+ count_compartments ()
+ check_vacancy()
Write a python program to implement the following:
count_compartments()- returns the total number of compartments
 in the train
check_vacancy()-returns the count of the compartments in which
 more than 50% of the seats are vacant
Note : Compartment list is maintained as a linked list where 
data in each node refers to a compartment.

compartment1=Compartment("SL",250,400)
compartment2=Compartment("2AC",125,280)
compartment3=Compartment("3AC",120,300)
compartment4=Compartment("FC",160,300)
compartment5=Compartment("1AC",100,210)
'''
class Node:
    def __init__(self,name,total_seats,num_passengers):
        self.name=name
        self.total_seats=total_seats
        self.num_passengers=num_passengers
        self.next=None

class Compartment:
    
    def __init__(self):
        self.start_node=None

    def insert_at_end(self,name,total_seats,num_passengers):
        new_node=Node(name,total_seats,num_passengers)
        if self.start_node is None:
            self.start_node=new_node
            return
        n=self.start_node
        while n.next is not None:
            n=n.next
        n.next=new_node
        
class Train:
    def __init__(self,train_name,compartment_list):  # to be added
        #self.start_node=None
        self.train_name=train_name
        self.compartment_list=compartment_list
        
    

    def get_train_name(self):
        return self.train_name

    def get_compartment_list(self):
        if self.compartment_list is None:
            print("List is Empty")
        else:
            n=self.compartment_list
            while n is not None:
                print(n.name,n.total_seats,n.num_passengers)
                n=n.next

    def count_compartments(self):
        if self.compartment_list is None:
            print("There are 0 compartments present in the list")
        else:
            n=self.compartment_list
            count=0
            while n :
                count+=1
                n=n.next
            return count
                
    def check_vacancy(self):
        if self.compartment_list is None:
            print("List is Empty")
        else:
            n=self.compartment_list
            count=0
            while n is not None:
                if n.num_passengers < n.total_seats*0.5:
                    count+=1
                n=n.next
            print("Vacancy =",count)

                


s=Compartment()   #seats,passengers
s.insert_at_end("SL",250,100)
s.insert_at_end("2AC",125,280)
s.insert_at_end("3AC",120,300)
s.insert_at_end("FC",160,300)
s.insert_at_end("1AC",100,210)

t=Train("Rajdhani Express",s.start_node)

print("Name of the Train is :",t.get_train_name())
#s.get_compartment_list()
print("There are ",t.count_compartments(),"no. of compartments")

t.check_vacancy()
