class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def isempty(self):
        if self.head is None:
            return False
        return True

    def insert_at_end(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
        else:
            c=self.head
            while c.next is not None:
                c=c.next
            c.next=node
            
    def traverse(self):
        if self.head is None:
            print("List has no elements")
            return
        else:
            n=self.head
            while n is not None:
                print(n.data," ")
                n=n.next
                
    def make_a_loop(self):
        nn=self.head
        n=self.head
        while nn.next is not None:
            nn=nn.next
        nn.next=n.next.next
        
        
s=LinkedList()
s.insert_at_end(1)
s.insert_at_end(2)
s.insert_at_end(3)
s.insert_at_end(4)
s.insert_at_end(5)
s.insert_at_end(6)
s.insert_at_end(7)
s.insert_at_end(8)

s.make_a_loop()



s.traverse()
