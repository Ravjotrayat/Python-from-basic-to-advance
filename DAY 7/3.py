class Evenly:
    def __init__(self,start,stop,size):
        self.__start=start
        self.__stop=stop
        self.__size=size
        self.__elements=[None]*self.__size
        self.__rear=-1
        self.__front=0
        self.__elements2=[None]*self.__size
        self.__rear2=-1
        self.__front2=0

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
        
    def check(self):
        for i in self.__elements:
            if self.check2(i,self.__start,self.__stop):
                self.__rear2+=1
                self.__elements2[self.__rear2]=i
            else:
                pass

    def check2(self,i,start,stop):
            for j in range(start,stop+1):
                if i%j==0:
                    pass
                else:
                    return False
            return True
        
    def display(self):
        for i in range(self.__front2,self.__rear2+1):
            print(self.__elements2[i])
        
start=1
stop=10
size=5
s=Evenly(start,stop,size)
s.enqueue(13983)
s.enqueue(10080)
s.enqueue(7113)
s.enqueue(2520)
s.enqueue(2500)
s.enqueue(33)
s.check()
s.display()


