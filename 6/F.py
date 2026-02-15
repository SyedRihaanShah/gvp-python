# Create dictionary
numbers = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40
}

# Sum all values
total = 0

for value in numbers.values():
    total += value

# Display result
print("Sum of all items:", total)