import time 

user = int(input("Which table you want to print"))


for i in range(1, 13):
    f = open(f'{user}_table.txt', 'a')
    f.write(f'{user} x {i} = {user * i} \n')
    f.close()

time.sleep(3)
print(f"Your {user} table has been created succesfully !")