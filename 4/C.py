n = int(input("what is n in your nxn matrix: "))

matrix = []

for i in range(n):
    row = []
    for j in range(n):
        value = int(input(f"Enter the value of [{i + 1}][{j + 1}]"))
        row.append(value)
    matrix.append(row)

print("Your matrix is: ")
for row in matrix:
    print(row)