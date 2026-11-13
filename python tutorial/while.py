#while loop is used to execute a block of code repeatedly as long as a certain condition is true. The syntax for a while loop is as follows:
# while condition:
i=0
while i<10:
    print(i)
    i+=2

i=0
while i<10:
    if i==5:
        break
    print(i)
    i+=1

# exercise 
password=input("Enter your password : ")
while password!="python":
    print("Incorrect password")
    password=input("Enter your password : ")
print("Correct password")