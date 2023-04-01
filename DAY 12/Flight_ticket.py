'''
Write a python program to help an airport manager to generate
 few statistics based on the ticket details available for a 
day.
Go through the below program and complete it based on the comments mentioned in it.
Note: Perform case sensitive string comparisons wherever necessary.
#Sample ticket list - ticket format: "flight_no:source:destination:ticket_no"
#Note: flight_no has the following format - "airline_name followed by three digit number

#Global variable
ticket_list=["AI567:MUM:LON:014","AI077:MUM:LON:056","BA896:MUM:LON:067","SI267:MUM:SIN:145","AI077:MUM:CAN:060","SI267:BLR:MUM:148","AI567:CHE:SIN:015","AI077:MUM:SIN:050","AI077:MUM:LON:051","SI267:MUM:SIN:146"]
print(find_passengers_flight("AI"))
print(find_passengers_destination("LON"))
find_passengers_per_flight()
print(sort_passenger_list())'''

ticket_list=["AI567:MUM:LON:014","AI077:MUM:LON:056","BA896:MUM:LON:067",
             "SI267:MUM:SIN:145","AI077:MUM:CAN:060","SI267:BLR:MUM:148",
             "AI567:CHE:SIN:015","AI077:MUM:SIN:050","AI077:MUM:LON:051",
             "SI267:MUM:SIN:146"]

def find_passengers_flight(a):
    print("Passengers List with",a,"Flight")
    for i in ticket_list:
        s=i.split(":")
        temp=s[0][0:2]
        if temp == a:
            print(i)
    print()       


def find_passengers_destination(b):
    print("Destination of Passengers with",b,"Place")
    for i in ticket_list:
        s=i.split(":")
        if b==s[2]:
            print(i)
    print()
    
def find_passengers_per_flight():
    print("Passengers per Flight")
    t=set()
    l=[]
    for i in ticket_list:
        s=i.split(":")
        l.append(s[0])
        t.add(s[0])
    for i in t:
        count=0
        for j in l:
            if i==j:
                count+=1
        print(i,count)
def sort_passenger_list():
    print("\nSorted Passenger List")
    ticket_list.sort()
    for i in ticket_list:
        print(i.split(":"))

find_passengers_flight("AI")
find_passengers_destination("LON")
find_passengers_per_flight()
sort_passenger_list()
