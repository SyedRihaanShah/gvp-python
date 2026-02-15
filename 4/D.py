user_list = []
even_list = []

n = int(input("Number of elements: "))

for i in range(n):
    value = int(input("Enter: "))
    user_list.append(value)

for num in user_list:
    if num % 2 == 0:
        even_list.append(num)

print(even_list)