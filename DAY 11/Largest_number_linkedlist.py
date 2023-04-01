class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            n.next=new_node
            
    def display(self):
        if self.head is None:
            print("List is Empty")
            return
        else:
            n=self.head
            while n is not None:
                print(n.data," ")
                n=n.next
            
    def largest(self,num):
        if self.head is None:
            print("List is Empty")
            return
        else:
            n=self.head
            c=0
            loc=0
            maxx=n.data
            while n is not None:
                if n.data >maxx:
                    maxx=n.data
                    loc=c
                n=n.next
                c+=1
        n=self.head
        for i in range(0,loc):
            n=n.next
            
        n.data=num
            
        
s=LinkedList()
s.insert_at_end(4)
s.insert_at_end(1)
s.insert_at_end(109)
s.insert_at_end(15)
s.insert_at_end(19)
s.display()
print()
s.largest(999)
s.display()
