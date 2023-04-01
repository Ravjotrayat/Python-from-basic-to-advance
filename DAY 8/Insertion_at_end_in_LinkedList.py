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

    '''def atbeginning(self,newdata):
        Newnode=Node(newdata)
        Newnode.nextval=self.headval
        self.headval=Newnode'''

    def Atend(self,newdata):
        Newnode=Node(newdata)
        if self.headval is None:
            self.headval=Newnode
            return
        laste=self.headval
        while laste.nextval:
            laste=laste.nextval
        laste.nextval=Newnode
        
list=SLinkedlist()
list.headval=Node("Mon")

e2=Node("Tue")
e3=Node("Wed")
list.headval.nextval=e2
e2.nextval=e3
list.listprint()
print()
#list.atbeginning("sun")
list.Atend("Sun")
list.listprint()
