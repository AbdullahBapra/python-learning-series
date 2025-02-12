





# We can use loops in programming to execute a block of code repeatedly until a specified condition is met.
# 
# 



# while loop – Used when we don’t know exactly how many times we need to repeat, but we have a condition that decides when to stop.

a = 1

while(a<8):
    print("abdullah",a)
    a += 1



 

fruits = ["apple", "banana", "amrod", "banaspati"]





 
i = 0

while (i<len(fruits)):
    print(fruits[i])
    i += 1



 
#  for loop – Used when we know how many times we want to repeat something.

# range function is used in python genertae a sdequance a number

for i in range(100):
    print("abdullah",i)





# for loop with else


a = [1,2,3]

for item in a:
    print(item)
else:
    print("done")



# break statment in for Loop 


for i in range(300):
    if(i == 85):
        break  # this statment is braek the loops exit the loop right now
    print(i)



# contiionus statment in for loop 

for i in range(56):
    if(i == 34):
        continue # skip the iteration
    print(i)





# pass statment in for loops 



for i in range(56):
     pass # without pass thre prgrammm give a error


x = 0

while(x<100):
    print(x)
    x += 1
