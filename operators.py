# Python Operators - Complete

# 1. Arithmetic Operators
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponent:", a ** b)
print("Floor Division:", a // b)

# 2. Comparison (Relational) Operators
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater or Equal:", a >= b)
print("Less or Equal:", a <= b)

# 3. Logical Operators
x = True
y = False

print("AND:", x and y)
print("OR:", x or y)
print("NOT x:", not x)

# 4. Assignment Operators
c = 5
c += 2
print("+= :", c)

c -= 1
print("-= :", c)

c *= 3
print("*= :", c)

c /= 2
print("/= :", c)

# 5. Bitwise Operators
m = 5   # 101
n = 3   # 011

print("Bitwise AND:", m & n)
print("Bitwise OR:", m | n)
print("Bitwise XOR:", m ^ n)
print("Bitwise NOT:", ~m)
print("Left Shift:", m << 1)
print("Right Shift:", m >> 1)

# 6. Membership Operators
numbers = [1, 2, 3, 4]

print("2 in list:", 2 in numbers)
print("5 not in list:", 5 not in numbers)

# 7. Identity Operators
p = [1, 2, 3]
q = p
r = [1, 2, 3]

print("p is q:", p is q)
print("p is r:", p is r)
print("p is not r:", p is not r)
