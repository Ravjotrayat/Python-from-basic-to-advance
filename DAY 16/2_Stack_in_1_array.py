# Implement 2 stacks using 1 array
class Stack:
    def __init__(self,capacity):
        self.capacity=capacity
        self.top1=-1
        self.elements=[None]*self.capacity
        self.top2=(self.capacity//2)-1
        
    def is_empty1(self):
        if self.top1==-1:
            return True
        return False

    def pop1(self):
        if self.is_empty1():
            pass
        else:
            #data=self.elements[self.top1]
            self.top1=self.top1-1
            #return data
        
    def is_full1(self):
        if self.top1==self.top2:
            return True
        return False

    def push1(self,data):
        if self.is_full1():
            print("Stack 1 is full")
        else:
            self.top1+=1
            self.elements[self.top1]=data

    def is_empty2(self):
        if self.top2==(self.capacity//2)-1:
            return True
        return False
    
    def is_full2(self):
        if self.top2==self.capacity-1:
            return True
        return False
            
    def push2(self,data):
        if self.is_full2():
            print("Stack 2 is full")
        else:
            self.top2+=1
            self.elements[self.top2]=data

    def pop2(self):
        if self.is_empty2():
            pass
        else:
            self.top2=self.top2-1

    
    def display1(self):
        if self.is_empty1():
            print("The Stack 1 is empty")
        else:
            index=self.top1
            index2=self.top2
            print("Stack 1 :",end=" ")
            while index>=0:
                print(self.elements[index],end=" ")
                index-=1
                
    def display2(self):
        print()
        if self.is_empty2():
            print("The Stack 2 is empty")
        else:
            index=self.top2
            print("Stack 2 :",end=" ")
            while index>(self.capacity//2)-1:
                print(self.elements[index],end=" ")
                index-=1
s=Stack(10)

s.push1(10)
s.push1(20)
s.push1(30)
s.push1(40)
s.push1(50)
#s.push1(100)

s.push2(1)
s.push2(2)
s.push2(3)
s.push2(4)
s.push2(5)
#s.push2(6)
s.display1()
s.display2()
print()
print()

s.pop1()
s.display1()
s.pop2()
s.display2()




