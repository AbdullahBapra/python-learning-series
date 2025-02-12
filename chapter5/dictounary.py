

# We can use a dictionary to store data in key-value form, allowing efficient retrieval, modification, and organization of related information.



# Dictionary is mutable, meaning we can change the dictionary's keys and values by adding, updating, or deleting key-value pairs dynamically.


info = {
   "name" : "abdullah",
   "age" : 45,
   "class" : 11,
   "father_name" : "faheem"    
}

# print(type(info))


# print(info)




# # Accessing dictionary values
 
# print(info["name"])

# print(info["age"])



# # Adding a new key-value pair


# info["city"] = "karachi"



# print(info)


# # Updating a key-value pair


# info["age"] = 50

# print(info)


# info.update({"age": 55})

# print(info)


# # Deleting a key-value pair


# del info["age"]

# print(info)


# info.pop("city")


# print(info)

print(info.get("name2")) #print none

print(info["name"]) # prinr an error