user_str = input("Enter your string: ")

#some useful string functions 
print(user_str)

print(user_str.strip())#strip() is a string method used to remove unwanted characters from the beginning and end of a string.

print(user_str.capitalize())#makes the first character capital 

print(user_str.lower())#makes all characters lowercase

print(user_str.upper())#makes all the string uppercase

demo_str = "I like python bcoz its better than c++"

print(demo_str.replace('python', 'C++'))#replaces a string with another

print(demo_str.find('p')) #finds the first index of the following character 

print(demo_str.count('t'))