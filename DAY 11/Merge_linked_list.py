#Merge 2 linkedlist at certain position
class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.start=None

    def insert_at_end(self,data):
        new_node=Node(data)
        if self.start is None:
            self.start=new_node
            return
        n=self.start
        while n.next is not None:
            n=n.next
        n.next=new_node

    def get_max_size(self):
        if self.start is None:
            return 0
        else:
            c=0
            n=self.start
            while n is not None:
                c+=1
                n=n.next
            return c

    def traverse_list(self):
        n=self.start
        while n:
            print(n.data,end=" ")
            n=n.next
        print()

def insert_at_position(s1,s2,n):
    n2=s2.get_max_size()  
    n1=s1.get_max_size()

    if n==0:
        z=s2.start
        while z.next is not None:
            z=z.next
        z.next=s1.start
        s1.start=s2.start
        return

    if n >=s1.get_max_size():
        z=s2.start
        while  z is not None:
            s1.insert_at_end(z.data)
            z=z.next
        return
                
    q=s1.start
    for j in range(1,n):
        q=q.next
    p=q.next
    
    q.next=s2.start
    o=s2.start
    while o.next is not None:
        o=o.next
    o.next=p  
    
s1=LinkedList()
s1.insert_at_end(1)
s1.insert_at_end(2)
s1.insert_at_end(4)
s1.insert_at_end(3)
s1.insert_at_end(5)
s1.traverse_list()
s2=LinkedList()
s2.insert_at_end(9)
s2.insert_at_end(8)
s2.insert_at_end(11)
s2.traverse_list()
n=1
m=insert_at_position(s1,s2,n)
s1.traverse_list()
