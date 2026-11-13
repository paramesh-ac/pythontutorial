# polymorphism which means same name but different method 

class developer:
    def dev(self):
        print("developer is developing the code")
class tester(developer):
    def test(self):
        print("tester is testing the code")
        super().dev()
class update:
    def upd(self):
        print("updating the code")


# c=tester()
# c.test()

c=update()
c.upd()