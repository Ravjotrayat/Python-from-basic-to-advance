#
class Wecare:
    def __init__(self,iid,typ,cost):
        self.__iid=iid
        self.__typ=typ
        self.__cost=cost
        self.__pre_amount=None
        self.set_premium_amount(self)
        
    def set_premium_amount(self,typ):
        if self.__typ=="Two Wheeler":
            self.__pre_amount=0.02*self.__cost
        elif self.__typ=="Four Wheeler":
            self.__pre_amount=0.06*self.__cost
        else:
            self.__pre_amount="Error in entering the Choise"
     
    def get_id(self):
        return self.__iid

    def get_tyy(self):
        return self.__typ

    def get_cos(self):
        return self.__cost

    def get_vehicle(self):
        return self.__pre_amount
    
s1=Wecare(101,"Two Wheeler",3000)
#s1.set_premium_amount()
print("Vehicle ID = ",s1.get_id())
print("Type = ",s1.get_tyy())
print("Cost = ",s1.get_cos())
print("Premium Amount =",s1.get_vehicle())





    
    
