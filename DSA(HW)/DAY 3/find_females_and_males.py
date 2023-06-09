class Queue:
    def __init__(self,size):
        self.size=size
        self.elements=[None]*self.size
        self.front=0
        self.rear=-1

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
            print("No more data can be Entered")
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

    def max_size():
        return self.size
    
class People:
    
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def calculate():
        for i in range(s1.front+1,s1.rear+1):
            if s1.elements[i].gender=="Female":
                print(s1.elements[i].name,s1.elements[i].age)

    

people1=People("Jack",25,"Male")
people2=People("Tom",30,"Male")
people3=People("Asha",27,"Female")
people4=People("Henry",27,"Male")
people5=People("Tina",27,"Female")

s1=Queue(5)
s1.enqueue(people1)
s1.enqueue(people2)
s1.enqueue(people3)
s1.enqueue(people4)
s1.enqueue(people5)

People.calculate()
#Output shouble be who are male and their name with age

