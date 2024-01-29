# Change Tuple Values
#  Tuples are unchangeable, or immutable as it also is called.
x = ("fariza" , "sultan" , "arai")
y = list(x)
y[1] = "mansur"
x = tuple(y)

print(x)
# Add Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y) 
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = ("orange",) #(comman)
thistuple += y

print(thistuple)

# Remove Items
x = ("fariza" , "sultan" , "arai")
y = list(x)
y.remove ("sultan") #без = просто в ()
x = tuple(y)
print(x)

delete = ("apple", "banana", "cherry")
del delete
print(delete) #this will raise an error because the tuple no longer exists
# (mistake)