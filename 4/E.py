user_list = []

n = int(input("Number of elements you want:"))

for i in range(n):
    value = (input("Enter:"))
    user_list.append(value)

length = list(map(len, user_list))
print(length)