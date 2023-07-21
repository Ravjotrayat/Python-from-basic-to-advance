# Some times shows the error as well like in "{}}{}{}}{}" Actual output:
# Unbalanced ,output given : Balanced

class Stack:
    def __init__(self,size):
        self.size=size
        self.elements=[None]*self.size
        self.top=-1

    def push(self,data):
        if data=='(' or data == '{' or data=="[":
            self.top+=1
            self.elements[self.top]=data
        else:
            
            if self.elements[self.top]=='(' and data==')':
                self.top-=1
            elif self.elements[self.top]=='{' and data=='}':
                self.top-=1
            elif self.elements[self.top]=='[' and data==']':
                self.top-=1
            
    def display(self):
        if self.top==self.size%2-1:
            print("balanced")
            
p=input("Enter the parenthesis\n")
if len(p)%2==0:
      s=Stack(len(p))
      for i in p:
          s.push(i)
      s.display()  
else:
    print("Unbalanced")
