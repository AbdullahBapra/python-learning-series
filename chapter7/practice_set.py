
# 1 

# number = int(input("enter a number"))

 
# for num in range(1,11):

#     print(f"{number} X {num} = {number * num}")


#     # 2 


# l = ["abdull", "ahad","samd","faheem"]

# for i in l:
#     if(i.startswith("a")):
#         print(i)




# 3

# number = int(input("enter a number"))

# n = 0

# while(n<11):
    
#     print(f"{number} X {n} = {number * n}")
#     n += 1
 



# # 4



# n = int(input("enter a number"))

# for i in range(2,n):
#     if(n%i) == 0:
#         print("number is not a prime")
#         break
# else:
#     print("number is prime")



# 5


# n = int(input("enter a nmber"))

# i = 1
# sum = 0

# while(i<=n):
#     sum += i
#     i +=1
     
# print(sum)






# # 7



# n = int(input("enter a nmber"))

# for i in range(1,n+1):
#     print(" "* (n-i), end="")
#     print("*"* (2*i-1), end="")
#     print("")
          

# If we input the number 5, the output will be:
#     *    
#    ***   
#   *****  
#  ******* 
# *********
# This creates a pyramid pattern where each row has centered stars,
# increasing in count as we move downward.


 




 

# n = int(input("enter a nmber"))

# for i in range(1, n+1):
#      if(i == 1 or i == n):
#       print("*" * n, end="")

#      else:
#       print("*",end="")
#       print(" " * (n-2), end="")
#       print("*" , end="")

#      print("")


# If we input the number 5, the output will be:
# *****
# *   *
# *   *
# *   *
# *****
# This creates a hollow square pattern where the first and last rows are fully filled,
# while the middle rows have stars only at the beginning and end.






# n = int(input("Enter a number: "))

# for i in range(1, n + 1):
#     if i == 1 or i == n:
#         print("*" * n, end="")
#     else:
#         print("*", end="")
#         print(" " * (n - 2), end="")  # ✅ Corrected (Added space)
#         print("*", end="")
#     print("")  # Move to the next line


















# enumerate() in Python
# The enumerate() function helps you loop through a list (or any iterable) while keeping track of the index and value at the same time.

# fruits = ["Apple", "Banana", "Cherry"]

# for i in range(len(fruits)):
#     print(f"Index {i}: {fruits[i]}")


# OUTPUT
# Index 0: Apple  
# Index 1: Banana  
# Index 2: Cherry  


   
# zip() in Python
# The zip() function allows you to loop over multiple lists (or iterables) at the same time.



# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 22]

# for i in range(len(names)):
#     print(f"{names[i]} is {ages[i]} years old")


# OUTPUT
# Alice is 25 years old  
# Bob is 30 years old  
# Charlie is 22 years old  




# for i in range(5):
#      print("*" * i)



for i in range(5):
    print("*" * (6 - i))

 




for i in range(1,21):
    if i  % 2 == 0:
        print(i)





# for i in range(1,6):
#      print(" "* (5-i), end="")
#      print("*" * (2*i-1),  end="")
#      print("")






for i in range(6,0,-1):
     print(" "* (5-i), end="")
     print("*" * (2*i-1),  end="")
     print("")



