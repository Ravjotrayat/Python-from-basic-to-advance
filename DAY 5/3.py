# object of pizzaservice(calculate_pizza_cost),
# doordelivery(calculate_pizza_cost)
class Customer:
    def __init__(self,quality):
        self.quantity=quantity
        validate_quantity(self)

    def validate_quantity(self):
        if self.quantity>=1 and self.quantity<=5:
            return True
        else:
            return False

class Pizzaservice:
    def __init__(self,additional_toppings,size,door_delivery):
        self.tt=100
        self.additional_toppings=additional_toppings
        self.size=size
        self.order=None
        self.pizza_id=None
        self.i=101
        self.cost=None
        self.total=None   # total cost after adding the delivery
        self.door_delivery=door_delivery   #in km
        validate_pizza_type()

    def validate_pizza_type(self):
        if self.size=='small' or self.size=='Small':
            self.order='s'
            calculate_pizza_cost()
        elif self.size=='medium' or self.size=='Small':
            self.order='m'
            calculate_pizza_cost()
        else:
            print("Invalid Size")
            print("Pizza Cost= ",-1)

    def calculate_pizza_cost(self):
        self.pizza_id=self.order+str(self.i)
        self.i=self.i+1
        if self.order=='s':
            if self.additional_toppings=True:
                self.cost=150+35
            else:
                self.cost=150
        else:
            if self.additional_toppings=True:
                self.cost=200+50
            else:
                self.cost=200
                
        #validate pizza type,cost, quantity #pizza_cost(att.)
        #generate => service_id(att.)starting from 100 example s101,m1

class Doordelivery:
    if self.door_delivery=>=1 and selfdoor_delivery<=10:
        print("Delivery is possible")
        validate_distance_in_kms()
    else:
        print("Delivery is not possible")

        def validate_distance_in_kms(self):
            if self.delivery<=5:
                self.total= 5+ self.cost
            elif self.delivery>5 and self.delivery<=10:
                self.total=5+7+self.cost
            else:
                self.total=-1
    
        
                
        
            









            
