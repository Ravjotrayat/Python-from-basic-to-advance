class Node:
    def __init__(self,name,reserved_seats,total_seats):
        self.name=name
        self.reserved_seats=reserved_seats
        self.total_seats=total_seats
        self.next=None

        
class Compartment:  
    def __init__(self):
        self.head=None

    def insert_at_end(self,name,reserved_seats,total_seats):
        new_node=Node(name,reserved_seats,total_seats)
        if self.head is None:
            self.head=new_node
            return
        n=self.head
        while n.next is not None:
            n=n.next
        n.next=new_node
        
class Train:
    def __init__(self,train_name,compartment_list):
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
                print(n.name,n.total_seats,n.reserved_seats)
                n=n.next


s=Compartment()
s.insert_at_end("SL",250,400)
s.insert_at_end("2AC",125,280)
s.insert_at_end("3AC",120,300)
s.insert_at_end("FC",160,300)
s.insert_at_end("1AC",100,210)

t=Train("Rajyarani Express",s.head)
t.get_compartment_list()
                
