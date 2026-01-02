# Data Initialization and Conditional Statements

age : None
print("Hello World! ")
temp = input("Enter number:")
if(type(temp) is int):
    age = int(temp)
else:
    print("Idiot!")
print(f"age")

# Loops 
for i , k  in enumerate(range(5)):
    print(f"{i}{k}")

# List ( Dynamic Data Type Array )

data = [ "ordered" , "unordered" , "funky" , "corrupted"]

a , * b , c = data

print(f"{a}\n{b}\n{c}")

print(f"{data.sort()}")

# Tuples ( Immutable List )

point = (10,20,30)

# Dictonaries 

email = [
    {
        "emailId" : "vikassane@gmail.com"
    },
    {
        "emailId" : "yashsane@gmail.com"
    },
    {
        "emailId" : "ganeshmalekar@gmail.com"
    }
]

for key in email:
    print(key)

# Sets ( Avoids Duplicate Values )

fruits = { "Apple" , "APple" , "Apple" }
print(f"{fruits}")

# Functions 

def greet ():
    print("Hello MF!")

greet()

# File Handling 

file = open("./lang/data.csv","r+")
content = file.read()
print(content)

for line in file:
    print(f"{line}")

file.close()
