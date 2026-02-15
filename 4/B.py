test_list = [1,2,3,4,5,6,7]

test_list.append(8) # adds the given element to the last
print(test_list)

test_list.insert(4,10)# inserts the given item at a given index and the index is given first
print(test_list)

test_list.remove(10)#removes a given element
print(test_list)

test_list.pop(0)#removes the element at a given index
print(test_list)

print(test_list.index(4)) # gives the index of a given element

test_list.clear()#clears the list
print(test_list)