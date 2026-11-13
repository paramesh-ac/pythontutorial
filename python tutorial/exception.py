# exception handling is the process of handling error without stopping the program 

try:
    x=int(input("enter a number:"))
except:
    print("please enter only in numbers :")
else:
    print("Thank you sir !")
finally:
    print("the program is finished ")