num = int(input("Enter a number "))
def is_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
for i in range(1,num):
    print(is_even(i))