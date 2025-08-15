# number = int(input("Enter the number you want a table of: "))
# i =1 
# while i < 10:
#     print(number * i)
#     i = i + 1

import random

prediction = random.randint(1,10)
user = int(input("Enter a number "))
while prediction != user:
    if prediction < user:
        print("Your number is too high")
    else:
        print("Your number is too low")
    user = int(input("Enter again "))
print("You Won!")