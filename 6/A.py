# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

# i. Union
union_set = set1.union(set2)
print("\nUnion:", union_set)

# ii. Intersection
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# iii. Difference
difference_set = set1.difference(set2)
print("Difference (set1 - set2):", difference_set)

# iv. Symmetric Difference (Asymmetric Difference in question)
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference_set)