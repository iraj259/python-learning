# def power(a=1,b=1):
#     return a**b
# print(power(2,3))
# print(power(2))
# print(power())

# def g(y):
#     print(x)
#     print(x+1)
# x=5
# g(x)
# print(x)

# function as objects
def f(num):
    return num*2

print(f(4))

x=f
print(x(2))
del f
# the func got deleted here
print(f(4))
print(x(2))
