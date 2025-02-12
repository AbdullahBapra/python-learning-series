

# We can use sets in Python to store unique elements in an unordered collection with efficient operations like union, intersection, and difference.



a = {1,2,3 ,4 ,5 ,5} # we can code of sets like this

# print(type(a))

d = {} #its a empty dectounary 


# if we want to write empty sets we write this code

b = set()

# print(type(b))


 
num = {5,4,3,7,1,9,6,4}

# print(num)

 
#  1. Adding and Removing Elements


my_set = {1,2 ,3 ,4 ,5}


 
# my_set.add(8)

my_set.remove(4)

# print(my_set)




# 2. Set Operations (Union, Intersection, Difference, symmentic)

# 1. Union (|) – Combines Both Sets (No Duplicates)
 
set = { 1,2 ,3 ,4 }
set_2 = {1,2,5,7,4}
print(set.union(set_2))

print(set|set_2)


# 2. Intersection (&) – Common Elements


set = { 1,2 ,3 ,4 }
set_2 = {1,2,5,7,4}
print(set.intersection(set_2))

print(set&set_2)



# 3. Difference (-) – Elements Only in First Set



set = { 1,2 ,3 ,4 }
set_2 = {1,2,5,7,4}
print(set.difference(set_2))
print(set-set_2)




# 4. Symmetric Difference (^) – Elements in Either Set, But Not Both




set = { 1,2 ,3 ,4 }
set_2 = {1,2,5,7,4}
print(set.symmetric_difference(set_2))

print(set^set_2)



# Checking If One Set is a Subset or Superset
# Subset (<=) → Checks if all elements of one set exist in another.
# Superset (>=) → Checks if one set contains all elements of another.
 



A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

print(A <= B)  # True (A is a subset of B)
print(B >= A)  # True (B is a superset of A)

