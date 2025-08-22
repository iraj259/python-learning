def greet():
    print('hello')
greet()

def greet(name):
    print('hello', name)
greet('iraj')

def add(a,b):
    return a+b
print(add(5,5))

def greet(name='guest'):
    print(f"hello, {name}")
greet('')
greet('iraj')
