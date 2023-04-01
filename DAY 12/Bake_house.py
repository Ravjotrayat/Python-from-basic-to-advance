'''
The owner of a BakeHouse wants to keep track of the tables 
that are occupied in his cafe. Assume that there are 10 tables in his cafe numbered from 1 to 10. As and when a table is occupied, it must be added to the occupied_table_list and when a customer leaves, the corresponding table must be removed from the list.

BakeHouse
- occupied_table_list
_init_()
+ get_occupied_table_list()
+ allocate_table()
+ deallocate_table(table_number)
Write a python program to implement BakeHouse class. 
Represent occupied_table_list using an appropriate data 
structure.
Note: Table numbers should be maintained in ascending order in the occupied_table_list.
Tables should be allocated and de-allocated as mentioned in the example below:
Example: Suppose tables 1, 2, 3 and 4 are initially allocated. Now if a new customer arrives, he should be allocated table 5 and the table list should be accordingly updated. If now customer at table 2 leaves, table list should be accordingly updated and the next new customer should be allocated table 2 as it is the first free table.
Implement the allocation logic in allocate_table() method and de-allocation logic in deallocate_table() method.
'''
class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class BakeHouse:

    def __init__(self):
        self.head=None
        self.count=1

    def occupied_table_list(self):
        pass
    def get_occupied_table_list(self):
        if self.head is None:
            print("All tables are empty")
        else:
            n=self.head
            i=1
            while n is not None:
                print(i,"->",n.data," ")
                i+=1
                n=n.next
            print()
    def free(self):
        copy=self.head
        while copy is not None:
            if copy.data=="Free":
                return True
            copy=copy.next
    def entry_data(self):
        data=(input("Enter the data\n"))
        new=Node(data)
        if self.head is None:
            self.head=new
            return
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            n.next=new
    def allocate_table(self):
        if self.count<=10:
            
            if self.free():
                data=int(input())
                copy=self.head
                
                while copy.next is not None:
                    if copy.data=="Free":
                        copy.data=data
                        break
                    copy=copy.next
            else:
                self.entry_data()
            self.count+=1
        else:
            if self.free():
            
                dat=input("Enter the data\n")
                copy=self.head
                while copy.next is not None:
                    if copy.data=="Free":
                        copy.data=dat
                        break
                    copy=copy.next
                    
            else:
                print("All tables are Full")
                self.get_occupied_table_list()

    def deallocate_table(self):
        table_number=int(input("Table number\n"))
        if table_number ==1 :
            self.head.data ="Free"
            return 
        
        n=self.head
        for i in range(0,table_number-1):
            n=n.next
        n.data="Free"
s=BakeHouse()
while (1):
    print("1.) For Occupied Table List \n2.) For allocate_table \n3.) For Deallocate Table")
    n=int(input())
    if  n==1:
        s.get_occupied_table_list()
    if n==2:
        s.allocate_table()
    if n==3:
        s.deallocate_table()
    else:
        continue
