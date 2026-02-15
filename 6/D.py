# Create a dictionary
student = {
    "name": "Rihaan",
    "age": 18,
    "college": "GVPCE"
}

# Input key to check
key = input("Enter key to check: ")

# Check if key exists
if key in student:
    print("Key exists in dictionary")
else:
    print("Key does not exist in dictionary")