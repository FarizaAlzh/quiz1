# Remove Item
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

# .discard
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset) #{'apple', 'cherry'} 

# .pop()
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()
# remove a random item apple {'banana', 'cherry'}
print(x)

print(thisset)


# .clear()
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

# del
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)  #this will raise an error because the set no longer exists
