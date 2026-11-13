# conditions statements in python 
# condtions are used to check the condition and execute the code based on the condition
age=int(input("Enter your age : "))
if age>60:
    print("You are a senior citizen")
elif age>17:
    print("You are an adult")
elif age>12:
    print("You are a teenager")
elif age<0:
    print("You are not born yet")
else:
    print("You are a child")