

# recrusion is those who call itself again and until this condition is not stop 



 
def factorial(n):
     if n == 0 or n == 1:
          return 1
     return n * factorial(n - 1) 


print(factorial(6))

 
 

def num(n):
     if n == 0:
       print("done")
       return

     print(n)
     num(n - 1)

num(5)

