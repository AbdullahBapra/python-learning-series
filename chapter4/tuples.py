

# we can use tuples in a dictionary to store data that belongs together. For example, we can store the name of a person and their age in a single tuple, and then store that tuple in a dictionary as a value associated with a key that represents the person's ID. Here's an example:

# tuples is unmutable means we can not change the values of tuples by using index number.



# name = ("abdur", "rahman" , "ali")

# print(type(name))


# name = ("abdullah", "rahman" , "ali")

# print(name[0]) = "abdul" # it will give error because tuples is unmutable.

# print(name)


# if we create a tuple with only one element, we need to include a comma after the element value, like this:

#  my_tuple = (1) this is not a tuple because it has no comma after the element value.

my_tuple = (1,) #this is a tuple because it has a comma after the element value.

print(type(my_tuple))



# methods of tuples:




# count() method returns the number of times a specified value appears in the tuple.


name = ("abdullah", "rahman" , "ali")


print(name.count("abdullah"))


# index() method finds the first occurrence of the specified value.


name = ("abdullah", "rahman" , "ali")


print(name.index("rahman"))



# functions of tuples:


fruits = ("apple", "banana", "cherry")

print(len(fruits)) # len() function returns the number of items in the tuple.


print(max(fruits)) # max() function returns the item with the highest value.


print(min(fruits)) # min() function returns the item with the lowest value.


print(sum(fruits)) # sum() function returns the sum of all the items in the tuple.


# we can use the tuple() constructor to make a tuple.


fruits = tuple(("apple", "banana", "cherry")) # note the double round-brackets tuple() constructor.

print(fruits)