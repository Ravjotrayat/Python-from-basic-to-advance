#insert at position

class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def insert_at_first(self,value):
        new_node=Node(value)
        if self.isEmpty():
            self.head=new_node
        else:
            new_node.next=self.head
            new_node.prev=new_node
            self.head=new_node
    
    def insert_at_position(self,value,pos):
        l=self.head
        c=0
        while l is not None:
            c+=1
            if c==pos--1:
                break
            l=l.next
        if pos==1:
            self.insert_at_first(value)
        elif l is None:
            self.insert_at_end(value)
        elif l.next is None:
            self.insert_at_end(value)
        else:
            new_node=Node(value)
            new_node.next=l.next
            new_node.prev=l
            l.next=new_node
                
            
    def insert_at_end(self,value):
        new_node=Node(value)
        if self.isEmpty():
           self.head=new_node
        else:
            l=self.head
            while l.next is not None:
                l=l.next
            l.next=new_node
            l.prev=l
     
    def printList(self):
        temp=self.head
        while temp:
            print(temp.data,sep=",")
            temp=temp.next
            
s=LinkedList()
s.insert_at_end(2)
s.insert_at_end(3)
s.insert_at_end(4)
s.insert_at_end(5)
s.insert_at_end(6)
s.insert_at_end(7)

s.printList()

s.insert_at_position(200,3)
print()
s.printList()
