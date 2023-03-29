#delete from beginning,ending

class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def isEmpty(self):
        if self.head is None:
            return True
        return False

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

    def deletefromlast(self):
        if self.isEmpty():
            print("List is empty")
        elif self.head.next is None:
            self.head=None
        else:
            temp=self.head
            while temp.next.next is not None:
                temp=temp.next
            temp.next = None
            
    def printList(self):
        temp=self.head
        while temp:
            print(temp.data,sep=",")
            temp=temp.next

s=DoublyLinkedList()
s.insert_at_end(2)
s.insert_at_end(3)
s.insert_at_end(4)
s.insert_at_end(5)
s.insert_at_end(6)

s.printList()
print()

s.deletefromlast()
s.printList()
        
