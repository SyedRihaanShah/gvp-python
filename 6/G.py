num = int(input("Enter a number: "))

result = bin(num).count('1') % 2 == 0

print(result)