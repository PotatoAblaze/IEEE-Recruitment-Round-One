s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")

found = dict()

for c in s2:
    found[c] = True

for c in s1:
    if c not in found:
        print("Not Balanced")
        exit()

print("Balanced")
