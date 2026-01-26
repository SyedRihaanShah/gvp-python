def mul_of_numbers(a,b):
    return a * b

try:
    num1 = int(input("Enter number 1:"))
    num2 = int(input("Enter number 2:"))
except ValueError as e:
    print(e)


print(f"Product of {num1} and {num2} is {mul_of_numbers(num1,num2)}")