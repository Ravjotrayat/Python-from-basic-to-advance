class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
        
class SLinkedlist:
    def __init__(self):
        self.headval=None

    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval

    '''def Atend(self,newdata):
        Newnode=Node(newdata)
        if self.headval is None:
            self.headval=Newnode
            return
        laste=self.headval
        while laste.nextval:
            laste=laste.nextval
        laste.nextval=Newnode'''
    
    def inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        Newnode=Node(newdata)
        Newnode.nextval=middle_node.nextval
        middle_node.nextval=Newnode
        
list=SLinkedlist()
list.headval=Node("Mon")

e2=Node("Tue")
e3=Node("Thu")
list.headval.nextval=e2
e2.nextval=e3
list.listprint()
print()
#list.Atend("Sun")
list.inbetween(list.headval.nextval,"Wed")
list.listprint()
