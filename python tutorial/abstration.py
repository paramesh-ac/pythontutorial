# abstraction is the process of functions are working in side the class 

from abc import ABC,abstractmethod

class Bank:
    def ATM(self):
        pass

class SBI(Bank):
    def sbi_atm(self):
        print("money withdraw from sbi bank")

class HDFC(Bank):
    def hdfc_atm(self):
        print("money withdraw from hdfc bank")


c=SBI()
c.sbi_atm()
