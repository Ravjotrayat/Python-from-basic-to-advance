class shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material
al=shoe(1000,"canvas")
print(al)
print(al.price,al.material)
print(id(al))

