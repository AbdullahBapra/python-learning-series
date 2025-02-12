 # Types in Python are used to store different types of data such as integers, floats, strings, booleans, None, etc.


a = 10  # a is stored with integer value 10
print(type(a))  # <class 'int'>

b = 90.555  # b is stored with float value 90.555
print(type(b))  # <class 'float'>

c = "hello world"  # c is stored with string value "hello world"
print(type(c))  # <class 'str'>

d = True  # d is stored with boolean value True
print(type(d))  # <class 'bool'>

e = None  # e is stored with None value
print(type(e))  # <class 'NoneType'>



# covertion of data types in python  we can convert one data type to another data type in python if it is valid


# 1. int() function is used to convert a value to integer

a = 10.5
b = int(a)
print(b)  # 10


# 2. float() function is used to convert a value to float

a = 10
b = float(a)
print(b)  # 10.0


# 3. str() function is used to convert a value to string


a = 10
b = str(a)
print(b)  # '10'


# 4. bool() function is used to convert a value to boolean

a = 10
b = bool(a)
print(b)  # True


print(bool(""))  # Empty string, will print False
print(bool("apple"))  # Something inside the string, will print True
print(bool(0))  # Zero, will print False
print(bool(10))  # A number that's not zero, will print True



# input()function is used to take input from the user in python and it always returns a string value from the user


# a = int(input("Enter a number1: "))
# b = int(input("Enter a number2: "))
# c = a + b
# print(c)  


# PRACTICE SET



1. # Write a program to add two numbers in Python

a = 10
b = 90
c = a + b
print(c)


2 # Write a program to find remainder when a number is divided by z

a = 10
b = 5

print("the numer a is divided by b and the remainder is", a % b)


3. # check the type of the variable assigned using input() function

# a = input("Enter a number: ")
# print(type(a))


4 # use comaprison opesrtor to find out whether a given variable a is greater than b or not a = 34, b = 80

a = 34
b = 80

print(a>b)


5 # write a progam to find the average of two numbers entered by the user

# a = int(input("Enter a number1: "))
# a = int(input("Enter a number2: "))

# c = a + b // 2

print(c)



6 # write a program to calculate the square of a number entered by the user

a = int(input("Enter a number: "))

print(a ** 2)

 
 