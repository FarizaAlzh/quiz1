print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200 
b = 33
if b > a :
    print("b is greater than a")
else:
    print("b is not greater than a")

# Evaluate Values and Variables
print(bool("hello"))
print(bool(15) , "\n")

x = 15
print(bool(x) , "\n")

"""
In fact, there are not many values that evaluate to False, except empty values, such as 
(), [], {}, "", the number 0, and the value None. 
And of course the value False evaluates to False

"""

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj) , "\n")

# Functions can Return a Boolean
def fariza():
    return 0 

print(bool(fariza()))

def fari() :
   return False
if fari():
   print("YES")
else:
   print("NO")

"""
Python also has many built-in functions that return a boolean value, 
like the isinstance() function, which can be used to determine 
if an object is of a certain data type:
"""
x = 200
print(isinstance(x , float))
