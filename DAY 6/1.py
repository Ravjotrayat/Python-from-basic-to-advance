class OverdrawException(Exception):
    pass
class LimitReachedException(Exception):
    pass

class Account:
    def __init__(self,account_type,balance,min_balance):
        self.account_type=account_type
        self.balance=balance
        self.min_balance=min_balance

    def get_account_type(self):
        return self.account_type

    def get_balance(self):
        return self.balance

    def get_min_balance(self):
        return self.min_balance

    def set_balance(self,balance):
        self.balance=balance

class Customer:
    def __init__(self,customer_id, customer_name,age,account):
        self.customer_id=customer_id
        self.customer_name=customer_name
        self.age=age
        self.account=account
        
    def withdraw(self,amount):
        if amount>self.account.get_balance():
            raise OverdrawException("Amount to be withdraw is greater than account balance")
        elif self.account.get_balance() - amount < self.account.get_min_balance():
            raise LimitReachedException("Balance amount is less than min acc. balance")
        else:
            self.account.set_balance(self.account.get_balance()-amount)

    def take_card(self):
        print("Take card out from the ATM")

    def get_customer_id(self):
        return self.customer_id

    def get_customer_name(self):
        return self.customer_name

    def get_age(self):
        return self.age

    def get_amount(self):
        return self.account.get_balance()

class PrivilegedCustomer(Customer):
    def __init__(self,customer_id, customer_name, age, account,bonus_points):
        super().__init__(customer_id, customer_name, age, account)
        self.bonus_points=bonus_points

    def increase_bonus(self):
        if self.account.get_balance()>1000:
            self.bonus_points+=10
        else:
            self.bonus_points+=2
        
    def withdraw(self,amount):
        try:
            super().withdraw(amount)
        except OverdrawException as e:
            print(e)
        except LimitReachedException as e:
            print(e)
        finally :
            self.increase_bonus()
            self.take_card()
                
    def get_bonus_points(self):
        return self.bonus_points
    
account=Account("Savings",2000,500)
pc=PrivilegedCustomer(100,"Ravjot Singh",22,account,100)
pc.withdraw(500)
print("Bonus points",pc.get_bonus_points())
        


