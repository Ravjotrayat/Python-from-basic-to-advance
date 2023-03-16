class mobile():
    def __init__(self):
        print(id(self))
    def display(self):
        print("Displaying Details")
    def purchase(self):
        self.display()
        print("calculating price")
mobile().purchase()
            
