class Queue:
    def __init__(self,size):
        self.size=size
        self.elements=[None]*self.size
        self.rear=-1
        self.front=0

    def full(self):
        if self.rear==self.size-1:
            return True
        return False

    def empty(self):
        if self.front>self.rear:
            return True
        return False

    def enqueue(self,data):
        if self.full():
            print("Queue is Full")
        else:
            self.rear+=1
            self.elements[self.rear]=data
        
    def dequeue(self):
        if self.empty():
            print("It is empty")
        else:
            data=self.elements[self.front]
            self.front+=1
            return data

    def display(self):
        for i in range(self.front,self.rear+1):
            print(self.elements[i],end=" ")
            
    def max_size(self):
        return self.size

def even_queue(s1,s2,s3):
    a=s1.max_size()
    for i in range(0,a):
        a=s1.dequeue()
        if a%2==0:
            s2.enqueue(a)
        else:
            s3.enqueue(a)n
s1=Queue(7)
s1.enqueue(2)
s1.enqueue(7)
s1.enqueue(9)
s1.enqueue(4)
s1.enqueue(6)
s1.enqueue(5)
s1.enqueue(10)
s1.display()

s2=Queue(7) #Even
s3=Queue(7) #Odd
ss=even_queue(s1,s2,s3)
print("\nEven no:")
s2.display()
print("\nOdd no:")
s3.display()
