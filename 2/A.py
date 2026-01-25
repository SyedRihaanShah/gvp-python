try:
    user_num = int(input("Enter your number:"))

except ValueError as e :
    print(e)

middle_number = user_num

while(middle_number!= 1):
    middle_number -= 2

if(middle_number == 0):
    print(f"{user_num} is even number")

else :
    print(f"{user_num} is odd number")
