from collections import Counter

s = "aaaaaabbbbcccc"

n = int(input("Enter n: "))

freq = Counter(s)

result = freq.most_common(n)

print(result)