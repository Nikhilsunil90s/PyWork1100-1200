# Parameters ----- Memory Layout (Array Like Layout, Non-Array Layout) , Can be Changed or not

# Data Types
# Numbers ---- Non-Array Like Layout, Immutable (Cannot be changed)
x = 90
x = 897
y = x + 3 # last value will be overridden
print(x)
# Strings ---- Array Like Layouts, Immutable
s = 'Hello, World'
y = s.swapcase()
print(s)
# Boolean --- subclasses of integer , Non-ArrayLike Layout , Immutable
True + True

# Data Structures
# Arrays ----> 2 Arrays , Heterogenous Collections
# 1. Lists ---- Mutable, [ ]
# 2. Tuples --- Immutable , ( )

# Sets ----> { } , Non-Array Like Layout, Mutable as well Immtutable(frozenset)

# Dictionary ---> { key: value, key: value, key:value,... } # Array Like Layout, Mutable