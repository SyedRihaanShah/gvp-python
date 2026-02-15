# Creating iterables of varied sizes
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c']
list3 = [10, 20, 30, 40, 50]

# Group values using zip
grouped = list(zip(list1, list2, list3))

# Display result
print("Grouped values:")
print(grouped)