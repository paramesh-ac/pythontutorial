# file handling is the process of the storing the data in files permently...
file=open("data.txt","w")
file.write("hello this is paramesh achari")
file.close()

# syntax is file = open("filename","operation")
# file.wrire("")
# file.close()

# read operation 
file=open("data.txt","r")
print(file.read())
file.close()


# append operation in python 

file=open("data.txt","a")
file.write("this is paramesh. I am learning python right now ")
file.close()