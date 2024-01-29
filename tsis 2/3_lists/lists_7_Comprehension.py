# List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

# 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

# The Syntax
# newlist = [expression for item in iterable if condition == True]
newlist = [x for x in fruits]

# Iterable
newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

# Expression
newlist = [x.upper() for x in fruits]

newlist = ['hello' for x in fruits]

newlist = [x if x != "banana" else "orange" for x in fruits]