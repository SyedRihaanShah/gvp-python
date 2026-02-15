# Create two sets
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

print("Set 1:", set1)
print("Set 2:", set2)

# Check subset
if set1.issubset(set2):
    print("\nSet1 is a subset of Set2")
else:
    print("\nSet1 is not a subset of Set2")

# Check superset
if set2.issuperset(set1):
    print("Set2 is a superset of Set1")
else:
    print("Set2 is not a superset of Set1")