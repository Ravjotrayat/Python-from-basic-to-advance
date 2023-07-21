#Mini Project
q1="""Who is the best Indian Cricketer?
a. Rohit Sharma
b. Virat Kohli
c. M.S.Dhoni
d. Kapil Dev
"""

q2="""Who is the best Basketball player in NBA?
a. Lebron James
b. Stephen Curry
c. Kyrie Irving
d. Michael Jordan
"""
q3="""Who is the best Football player in World??
a. Sunil Chhetri
b. Neymar
c. Ronaldo
d. Messi
"""
q4="""Who is the Basketball captain of GIET University??
a. Ayush Sharma
b. Ravjot Singh
c. Ashish S.
d. Nitish Patnaik
"""
q5="""What is the name of our Super Coder trainer??
a. Sweeta
b. Faraz Asraf
c. Jyoti
d. 
"""
questions={q1:"c",q2:"d",q3:"a",q4:"b",q5:"d"}
print("Hi..! Whats your name??")
print("Hello",input(),"Welcome to the Quiz.\n")
count=0
for i in questions:
    print(i)
    a=input("Do u want to skip this question (yes/no)??")
    if a=='yes':
        continue
    print("Enter your answer")
    if input()==questions[i]:
        count+=1
        print("Hurray..! you score one point,your score is:",count)
    else:
        if count!=0:
            count-=1
            print("Oops..! you lose one point,you score becomes:",count)
        else:
            print("Your score remains the same:",count)
        
print("Your final score becomes :",count)
