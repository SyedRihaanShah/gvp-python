number_1 = int(input("Enter number 1 : "))
number_2 = int(input("Enter number 2 : "))

if number_1 > number_2:
    number_1, number_2 = number_2, number_1

if number_1 % 2 != 0 and number_2 % 2 != 0:
    number_1 = number_1 - 1
    number_2 = number_2 + 1

total = 0

for i in range(number_1 + 2, number_2, 2):
    total = total + i

print(total)