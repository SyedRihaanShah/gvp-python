# Creating tuples for two members
member1 = ("Rihaan", 20, "Hyderabad", "IIT Hyderabad")
member2 = ("Ayaan", 21, "Mumbai", "BITS Pilani")

# Display the tuples
print("Member 1 Tuple:", member1)
print("Member 2 Tuple:", member2)

# Concatenation of tuples
concatenated_tuple = member1 + member2
print("\nConcatenated Tuple:")
print(concatenated_tuple)

# Print first tuple n times
n = int(input("\nEnter number of times to print first tuple: "))

repeated_tuple = member1 * n

print("\nFirst tuple repeated", n, "times:")
print(repeated_tuple)