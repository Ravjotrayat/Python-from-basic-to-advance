# break     if we use break with for loop and else block,else block will not be exceuted
# if we dont have break,then else block will be executed
# Skipping is use by "continue" statement or pass
#empty classes and empty statement "pass" keywordn is used
for i in range(1,100):
    if i==50:
        break
    print(i,end=' ')
else:
    print("else block")
    
#Using pass statemnet
for i in range(1,101):
    if i!=50:
        pass
    print(i,end=' ')

