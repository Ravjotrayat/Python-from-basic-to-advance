
class Evaluate:
    def __init__(self,capacity):
        
        self.capacity=capacity
        self.top=-1
        self.array=[]

    def isempty(self):
        if self.top == -1:
            return True
        return False

    def peek(self):
        return self.array[-1]
    
    def pop(self):
        if self.isempty():
            return '$'
        else:
            data=self.array[self.top]
            self.top-=1
            return data

    def push(self,op):
        self.top+=1
        self.array.append(op)

    def evaluatepostfix(self,exp):
        for i in exp:
            if i.isdigit():
                self.push(i)
            else:
                val1=self.pop()
                val2=self.pop()
                self.push(str( eval(val2+i+val1) ) )
        return int(self.pop())        

exp= "231*+9-"
obj=Evaluate(len(exp))
print("%d"%obj.evaluatepostfix(exp))

OR

'''
class Evaluate:
    def __init__(self,cap):
        self.top = -1
        self.capacity = cap
        self.array = []

    def is_empty(self):
        if(self.top == -1):
            return True
        return False

    def peek(self):
        return self.array[-1]
    
    def pop(self):
        if(self.is_empty()):
            return "$"
        else:
            data = self.array[self.top]
            self.top -= 1
            return data

    def push(self, op):
        self.top +=1
        self.array.append(op)
    
    def evaluatePostFix(self, exp):
        
        for i in exp:
            if(i.isdigit()):
                self.push(i)
            else:
                val1 = self.pop()
                val2 = self.pop()
                self.push(str(eval((val2 + i + val1))))
        return int(self.pop())
    
if __name__ == "__main__":
    strs = "279*+9-"
    x = Evaluate(len(strs))
    print(x.evaluatePostFix(strs))

    '''
