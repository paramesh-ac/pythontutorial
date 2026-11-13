# loops are used to repeat a block of code multiple times. In Python, there are two main types of loops: for loops and while loops.
for i in range(5):
    print(i)

# printing even numbers from 1 to 10 using for loop
for i in range(1,11):
    if i%2==0:
        print(i)

# printing odd numbers from 1 to 10 using for loop
for i in range(1,11):
    if i%2 !=0:
        print(i)
print("Hello world!")

# for loop with else statement
for i in range(2,20,2):
    print(i)



for i in range(1,11):
    if i==5:
        pass
    print(i)


# break statement is used to exit the loop when a certain condition is met. When the break statement is executed, the loop terminates immediately, and the program continues with the next statement after the loop.
for i in range(1,11):
    if i==5:
        break
    print(i)

# continue 

for i in range(1,11):
    if i==5:
        continue
    print(i)
    
