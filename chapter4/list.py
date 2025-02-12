

# we can used list in store multiple values in a single variable. List is a collection which is ordered and changeable. Allows duplicate members. List is represented by square brackets. List is a collection data type


a = ["abdullah", 23, 5.5 , "karachi", True] # list can store multiple data types

print(a)

# list is mutable means we can change the values of list  by using index number of list


# functions of list:

# 1. append() : add the element in the end of list

name = ["abdullah", "ali", "ahmed", "umer"]

name.append("usman") # add usman in the end of list


print(name) # ['abdullah', 'ali', 'ahmed', 'umer', 'usman']


# 2. insert() : add the element in the specific index of list


fruits = ["apple", "banana", "mango", "orange"]

fruits.insert(2, "grapes") # add grapes in the 2nd index of list


print(fruits) # ['apple', 'banana', 'grapes', 'mango', 'orange']


# 3. remove() : remove the element from the list


fruits.remove("banana") # remove banana from the list


print(fruits) # ['apple', 'grapes', 'mango', 'orange']


# 4. pop() : remove the element from the specific index of list


fruits.pop(2) # remove the element from the 2nd index of list


print(fruits) # ['apple', 'grapes', 'orange']


# 5. clear() : remove all the elements from the list


fruits.clear() # remove all the elements from the list


print(fruits) # []


# 6. copy() : copy the list


fruits = ["apple", "banana", "mango", "orange"]


fruits1 = fruits.copy() # copy the list


print(fruits1) # ['apple', 'banana', 'mango', 'orange']


# 7. reverse() : reverse the list


fruits.reverse() # reverse the list



print(fruits) # ['orange', 'mango', 'banana', 'apple']


# 8. sort() : sort the list


fruits.sort() # sort the list


print(fruits) # ['apple', 'banana', 'mango', 'orange']


# 9. index() : return the index of specific element


print(fruits.index("mango")) # 2


# 10. count() : return the number of times the specific element is present in the list


print(fruits.count("mango")) # 1




# we have many other functions of list. you can check it by using dir(list) function in python shell or you can check it by using help(list) function in python shell
















# Without List Comprehension (Traditional For Loop)


numbers = [1, 2, 3, 4, 5]
squared_numbers = []
for num in numbers:
    squared_numbers.append(num ** 2)

print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
















# With List Comprehension (One-Liner Magic)


numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]

print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
























