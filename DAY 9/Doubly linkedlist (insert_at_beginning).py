#Doubly Linked List

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

    def length(self):
        temp=self.head
        count=0
        while temp:
            count+=1
            temp= temp.next
        return count

    def insert_at_beginning(self,value):
        new_node=Node(value)
        if self.isEmpty():
            self.head=new_node
        else:
            new_node.next=self.head
            new_node.prev=new_node
            self.head=new_node
`
    def printList(self):
        temp=self.head
        while temp:
            print(temp.data,sep=",")
            temp=temp.next

s=DoublyLinkedList()
s.insert_at_beginning(10)
s.insert_at_beginning(20)
s.insert_at_beginning(30)
s.insert_at_beginning(40)
s.insert_at_beginning(50)

s.printList()
print("Count=",s.length())
 
