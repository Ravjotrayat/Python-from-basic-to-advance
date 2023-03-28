class Queue:
    def __init__(self,size):
        self.__size=size
        self.__elements=[None]*self.__size
        self.__rear=-1
        self.__front=0
        
    def is_full(self):
        if self.__rear==self.__size-1:
            return True
        return False

    def is_empty(self):
        if self.__front>self.__rear:
            return True
        return False
    
    def enqueue(self,data):
        if self.is_full():
            print("Queue1 is Full")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def dequeue(self):
        if self.is_empty():
            print("Queue1 is Empty")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

        
    '''def display3(self):
        for i in range(self.__front3,self.__rear3+1):
            print(self.__elements3[i])'''

    def get_max_size(self):
        return self.__size

def merge(s,s2):
    a=s.get_max_size()
    b=s2.get_max_size()
    c=a+b
    s3=Queue(c)   #Queue call
    for i in range(min(a,b)):
        
    

s=Queue(3)

s.enqueue(3)
s.enqueue(6)
s.enqueue(8)
print(s.get_max_size())

s2=Queue(6)
s2.enqueue('b')
s2.enqueue('y')
s2.enqueue('u')
s2.enqueue('t')
s2.enqueue('r')
s2.enqueue('o')
print(s2.get_max_size())

s3=merge(s,s2) #function call
