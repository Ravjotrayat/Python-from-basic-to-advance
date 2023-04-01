class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if self.__rear==self.__max_size-1:
            return True
        return False

    def is_empty(self):
        if self.__front>self.__rear:
            return True
        return False

    def enqueue(self,data):
        if self.is_full():
            print("Queue is Full")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        for i in range(self.__front,self.__rear+1):
            print(self.__elements[i])

    def get_max_size(self):
        return self.__max_size

s=Queue(5)
s.enqueue(2)
s.enqueue(3)
s.enqueue(4)
s.enqueue(5)
s.enqueue(6)
s.display()
s.enqueue(4)
print("Element deleted",s.dequeue())
s.display()

            
            
        
