class mobile():
    def __init__ (self,brand,price):
        
        self.brand=brand
        self.price=price
        self.total_price=None
    def purchase(self):
        if self.brand=="Apple":
            discount=10
        else:
            discount=5
        self.total_price=self.price - self.price *(discount/100)
        print("Total price of ",self.brand,"mobile ",self.total_price)
        
    def amount_returned(self):
        return (self.price - self.total_price)
        
mob1=mobile("Apple",20000)
mob2=mobile("Samsung",10000)
mob1.purchase()
mob2.purchase()
print(mob1.amount_returned())
print(mob2.amount_returned())
        
