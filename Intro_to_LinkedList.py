oclass Node:
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
list=SLinkedlist()
list.headval=Node("Mon")

e2=Node("Tue")
e3=Node("Wed")
list.headval.nextval=e2
e2.nextval=e3
list.listprint()
