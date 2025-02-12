


# 1 


# def greatest(a , b, c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     elif(c>b and c>a):
#         return c
     
# print(greatest(4,6,3))
 



# 2 

# def farin(f):
#     return 5* (f - 32)/9

# f = int(input("entera number in f: "))
# print(farin(f))

# 3


print("abdullah ", end="")
print("bapra")



# 4 


def sum(a):
    if (a == 1):
        return 1
    return sum(a - 1) + a

print(sum(67))
    
    

# 5


# def pattern(n):
#     if n == 0:
#          print("done")
#          return
#     print("*" * n)
#     pattern(n - 1)


# print(pattern(5))




# # 6 

# def inch_to_cm(n):
#     return n * 2.45
# a = int(input("enter a numver"))
# print(f"a corecponding valuo of {inch_to_cm(a)}")
        
     
 
def rem(l , words):
    a = []
    for item in l:
        if item != words:
            a.append(item.strip(words))
    return a
        
l = ["abdullah", "faheem" , "areeb"]
print(rem(l , "ah"))



def mul(n):
      for l in range(1 ,11):
          print(f"{n} X {n} = { n * l}")


mul(5)
       
 
def rec(n):
    if n == 0:
        print("done")
        return
    return n * (n - 1)

print(rec(7))

    

def rev(word):
    return  "".join(reversed(word))

print(rev("hello"))
                
