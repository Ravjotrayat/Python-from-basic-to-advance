#Remove the duplicate record from the sorted linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,data):  #At the end
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        else:
            last=self.head
            while last.next:
                last=last.next
            last.next=new_node

    def printList(self):
        l=self.head
        while l:
            print(l.data)
            l=l.next

    def remove_duplicate(self):
        
        if self.head is None:
            print("Enter the Data")
            
        else:
            l=self.head
            while l.next is not None:
                if l.data==l.next.data:
                    l.next=l.next.next
                    continue
                l=l.next
                

s=LinkedList()
s.push(1)
s.push(2)
s.push(3)
s.push(3)
s.push(3)
s.push(4)
s.push(5)
s.printList()

s.remove_duplicate()
print()
s.printList()
