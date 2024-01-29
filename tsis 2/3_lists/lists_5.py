# Remove Specified Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# 
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index pop()
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# removes the last item.
thislist = ["apple", "banana", "cherry"] 
thislist.pop()
print(thislist)

# del keyword also removes the specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Clear the List
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)