def multiply(a,b):
    result = 0
    for i in range(b):
     result = result + a
    print(result)
multiply(3,4)

# recursion
def mul(a,b):
   if b==1:
      return a
   else:
      return a+mul(a,b-1)
print(mul(3,4))

