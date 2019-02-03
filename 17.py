#Write a Menu driven program in Python to implement simple banking application. Application should read the customer name, account number, initial balance, rate of interest, contact number and address field etc. Use Object Oriented Programming. It should have following methods. 
#createAccount()   2) deposit()  3) withdraw() 4) computeInterest() 

class bank:
    def __init__(self,name,number,bal):
        self.name=name
        self.number=number
        self.ini_bal=bal
    def depo(self,amt):
        self.ini_bal=self.ini_bal+amt
    def withd(self,amt):
        self.ini_bal=self.ini_bal-amt
    def interest(self):
        return self.ini_bal+(self.ini_bal*0.3)
    def display(self):
        print(self.ini_bal)

b = bank("Rajpreet","9769577063",15000)
b.depo(4500)
b.display()
b.withd(1000)
b.display()
print(b.interest())
