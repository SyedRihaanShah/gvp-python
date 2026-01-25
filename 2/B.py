User_list = []

Len_list = int(input("How many numbers you want to compare: "))

for i in range(0,Len_list):
    User_list.append(int(input()))

print(f"The largest number of {User_list} is {max(User_list)}")
#or you can use sort and get the number at the last index 