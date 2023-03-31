class Car:
    def __init__(self,model,year,reg_num):
        self.model=model
        self.year=year
        self.reg_num=reg_num

    def __str__(self):
        return f"{self.model} ({self.year}) - {self.reg_num}"
    
class Service:
    def __init__(self,car_list):
        self.car_list=car_list
        
    def get_car_list(self):
        return self.car_list
        

    def find_cars_by_year(self,year):
        result=[]
        for i in self.car_list:
            if i.year == year:
                result.append(i.model)
        return result

    def add_cars(self,new_car_list):
        self.car_list+=new_car_list
        self.car_list.sort(key=lambda car:car.year)

    def remove_cars_from_karnataka(self):
        self.car_list=[i for i in self.car_list
                        if not i.reg_num.startswith("KA")]

car_list=[ Car("Civic",2010,"MH1234"),
           Car("Accord",2011,"KA4321"),
           Car("City",2011,"GJ5678"),
           Car("CRV",2012,"MH5678")]
s=Service(car_list)
#print(s.get_car_list())
print([str(car) for car in s.get_car_list()])
print()
print(s.find_cars_by_year(2011))
print()
s.add_cars([Car("BRV", 2013, "DL1234")])

#print(s.get_car_list())
print([str(car) for car in s.get_car_list()])
print()
s.remove_cars_from_karnataka()

#print(s.get_car_list())
print([str(car) for car in s.get_car_list()])
print()
