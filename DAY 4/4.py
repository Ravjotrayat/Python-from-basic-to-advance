'''
class Example:
    def __init__(self,num):
        self.num=num
    def set_num(self,num):
        self.num=num
    def get_num(self):
        return self.num
obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())
'''
class book:
    def __init__(self):
        self.title=None
my_fav=book()
my_fav.title="Head first programming"
your_fav=book()
your_fav.title="Learn python the hard way"

my_fav.title="Learning Python"
print("1",my_fav.title)
print("2",your_fav.title)
