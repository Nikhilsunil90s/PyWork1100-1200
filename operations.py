# Operators 
# Arithmetic ---> +, * , - , /(true divide) , //(floor divide) , ceil , % (modulus - remainder) , **(raised to power)
# On Numbers
23 + 34
12 - 2
12 * 8
print(24 /5) # return float
print(24 // 7) # returns an integer nearest towards floor (down)
import math
print(math.ceil(24 / 7)) # nearest integer towards ceil (up)
print(round(34.344))
# % 
print(24 % 5)
print(3 ** 18)

# Hours to Day Calculator
# hours = int(input("Enter No. Of Hours : ")) # 43
# days = hours // 24
# extraHours = hours % 24
# print(days , " no. of Day(s) and" , extraHours , " no. of Extrahour(s)!")

# On Strings ----> + Concat, * Repeat (must be used with an intger)
print("Hello" + "QWERTY!")
print(100 + 200)
print('Hello ' * 10)

# On Boolean --- 
print(True + True)
print(2 ** False)
print(False - True)
print(23 / True)

#  Relational Operations --- return only boolean (True/ False)
# < ,> ,<= , >= 
# On Numbers
print(23 < 56)
print(23 > 89)
23 % 5 == 0
# On Strings --- only first char of both strings (ascii value)
print('apple' > 'apple')
# To check an ascii value of a char
print(ord('a') , ord('o'))
# 
print(chr(116))
# Equality Check ---- Loose Equality Check or STrict Equality Check