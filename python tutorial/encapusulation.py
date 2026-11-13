# encapsulation is the process of protecting the data under the function methods 

class Bank:
    def __init__(self):
        self.__balance=1000
    def display(self):
        print(self.__balance)
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        self.__balance-=amount
s1=Bank()


s1.withdraw(2000)
# s1.deposit(1000)
s1.display()