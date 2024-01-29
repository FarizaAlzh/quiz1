# Strings
print ("Hello")
print('Hello')

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Strings are Arrays
a = "Hello"
print(a[1])

# Looping Through a String
for x in "fariza" :
    print(x)

# Length String 
a = "Hello"
print(len(a))

# Check String 
txt = "The best things in life are free"
print("free" in txt)                     #True or False  IN

txt = "The best things in life are free"
if "best" in txt :
    print("YES")

# Check if NOT
txt = "The best things in life are free"
print("expensive" not in txt)             # NOT IN

txt = "The best things in life are free"
if "expensive" not in txt:
    print("The word expensive not in txt")
