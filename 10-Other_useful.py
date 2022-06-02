import os
os.system("cls")

# generate list
print("#"*40)
a = list(range(5, 20, 3))
print("Sequence:", a)

# list from string
print("-"*40)
a = "Eduard Buhali"
b = list(a)
print("List from String: ", b)

# set from string (only unique)
print("-"*40)
a = "Eduard Buhali"
b = set(a)
print("Set from String:", b)

# One line for
print("-"*40)
aItems = list(range(1, 10))
res = [(i**3) for i in aItems]
print("One line for (each array item to power of 3):", res)
print("#"*40)
