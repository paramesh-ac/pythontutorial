# inheritence means properties and methods are appiled from the parents class

class Employee:
    def worker(self):
        print("worker is working in the class")

class Tester(Employee):
    def Test(self):
        print("tester is testing the code ")
class develper(Employee):
    def dev(self):
        print("developer is developing the code")

s1=Tester()
s1.Test()
c=develper()
c.worker()
c.dev()