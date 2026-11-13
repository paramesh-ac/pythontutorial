# operators : which means performing the operation using the operators 
"""
1.arthimetic operators 
2.assignment operators 
3. logical operators 
4. comparison operators
5. membership operators
6. identity operators
"""

name="paramesh"
a=10
b=20
print(a+b,"addition")
print(a-b,"subtraction")
print(a*b,"multiplication")
print(a/b,"division")   
print(a%b,"modulus")
print(a**b,"exponential")   
print(a//b,"floor division")

# assignment operators 

x=10
print(x+5)
x+=5
print(x)
x-=5
print(x)
x*=5
print(x)
x/=5
print(x)
x//=5
print(x)
x%=5
print(x)
x**=5
print(x)


# comparison operators 
# answers will be in boolean values True or false 

y=10 
z=5

print(y>z,"greater than")
print(y<z,"less than")
print(y==z,"equal to")
print(y!=z,"not equal to")
print(y>=z,"greater than or equal to")
print(y<=z,"less than or equal to")

# logical operators and, or , not

a= True
b= False

print(a and b,"and operator")
print(a or b,"or operator")
print(not a,"not operator")


# membership operators
list1=[1,2,3,4,5]
print(3 in list1,"in operator")
print(6 not in list1,"not in operator")

# identity operators
x=5
y=5 # it is same memory location then x and y are same


print(x is y,"is operator")
print(x is not y,"is not operator"  )