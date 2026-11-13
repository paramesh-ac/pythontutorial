# # list is a ordered collection of items that can be of any data type. Lists are mutable, meaning you can change their content without changing their identity. They are defined by enclosing elements in square brackets [].
# l=[1,2,3,4,5]
# print(l)
# l[1]=10
# print(l)
# l.append(6)
# print(l)
# l.remove(3)
# print(l)    
# l.pop(3)
# print(l)
# l.clear()
# # print(l)

# list is ordered , mutable and allows duplicate elements. It is defined by enclosing elements in square brackets [].
a=[1,2,3,4,5]
b=["python","java","c++",3,4,5]

# string accessing 
print(a[0])
print(b[1])
print(b[-1])
print(b[-2])
print(a[1:4])# slicing
print(b[1:4])# slicing
print(a[::2])# slicing with step
print(a[::-1])# reverse string 
# adding the list 
a.append(2)
print(a)
a.insert(4,10)
print(a)
a.extend([40,44,33,44])
print(a)

# removing the string using, remove ,pop, del ,clear 
a.remove(44)
print(a)
a.pop()
print(a)
a.pop(3)
del a [1]
print(a)
a.clear
print(a)

# update the elements 
b[0]=2
print(b)
print(b.index(2))
b.extend([2,22,2,2])
print(b)
print(b.count(2))

print(2 in b)
print(0 not in b)

c=[50,40,30,20,10]
c.sort()
print(c)
c.sort(reverse=True)
print(c)
for i in c:
    print(i)

# while loop
# i=0
# while i > len(b):
#     print(i)
#     i+=i 

numbers = [10, 20, 30]

i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1

names = ["Python", "Java", "SQL"]

for index, value in enumerate(names):
    print(index, value)


x= [1,2,3,4,5]
y=[i**2 for i in x]
print(y)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])     # [1, 2, 3]
print(matrix[1][2])  # 6