def is_anagram(userstr1 , userstr2):
    return sorted(userstr1) == sorted(userstr2)
userstr1 = input("Enter your word to compare: ")
userstr2 = input("Enter your word to compare: ")

if is_anagram(userstr1, userstr2):
    print(f"These words {userstr1} and {userstr2} are anagrams ")

else:
    print("False")
