user_input  = int(input("Enter number :"))

for i in range (1, user_input + 1):
    print(" " * (user_input - i) + "*"*(2*i - 1))