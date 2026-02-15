# Existing dictionary
student = {
    "name": "Rihaan",
    "age": 20,
    "college": "IIT Hyderabad"
}

print("Original dictionary:")
print(student)

# Input new key and value
key = input("\nEnter new key: ")
value = input("Enter new value: ")

# Add new key-value pair
student[key] = value

# Display updated dictionary
print("\nUpdated dictionary:")
print(student)