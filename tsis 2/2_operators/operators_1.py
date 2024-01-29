# Arithmetic Operators
'''
+   Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	    x % y	(остаток)
**	Exponentiation	x ** y
//	Floor division  x // y (целое число)
'''
# Assignment Operators
'''
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	(в двоичной форме and ответ с цифрой)
|=	x |= 3	x = x | 3	(в двоичной форме or ответ с цифрой)
^=	x ^= 3	x = x ^ 3	(в двоичной форме xor ответ с цифрой 00,11 = 1 | 01,10 = 0)
>>=	x >>= 3	x = x >> 3	(сдвигает биты числа вправо на указанное количество позиций)
<<=
'''

# Comparison Operators
"""
==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y	
"""

#  Logical Operators
'''
and or not 
'''

# Identity Operators
"""
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y"""

# Membership Operators / not in / in 
x = ["apple", "banana"]
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list

# Bitwise Operators
#  & | ^ 

"""
Operator	
()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction	
<<  >>	Bitwise left and right shifts	
&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	Logical NOT	
and	AND	
or	OR"""