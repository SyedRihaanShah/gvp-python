# Input value of n
n = int(input("Enter value of n: "))

# Create dictionary
square_dict = {}

for x in range(1, n + 1):
    square_dict[x] = x * x


print(square_dict)