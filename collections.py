# Python Collections - Beginner Friendly


# -------- 1. LIST OPERATIONS --------
# Lists are ordered and mutable (changeable)

numbers = [10, 20, 30]

numbers.append(40)          # Adds element at end
print("After append:", numbers)

numbers.insert(1, 15)       # Inserts 15 at index 1
print("After insert:", numbers)

numbers.remove(20)          # Removes element 20
print("After remove:", numbers)

numbers.pop()               # Removes last element
print("After pop:", numbers)

numbers.sort()              # Sorts list
print("After sort:", numbers)

numbers.reverse()           # Reverses list
print("After reverse:", numbers)

# -------- 2. TUPLE OPERATIONS --------
# Tuples are ordered and immutable (cannot be changed)

colors = ("red", "green", "blue")

print("Tuple:", colors)
print("First element:", colors[0])   # Access element
print("Length:", len(colors))         # Length of tuple

# -------- 3. SET OPERATIONS --------
# Sets are unordered and store unique values

my_set = {1, 2, 3}

my_set.add(4)               # Adds element
print("After add:", my_set)

my_set.remove(2)            # Removes element
print("After remove:", my_set)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Union:", set1 | set2)        # Combines sets
print("Intersection:", set1 & set2) # Common elements
print("Difference:", set1 - set2)   # Difference

# -------- 4. DICTIONARY OPERATIONS --------
# Dictionaries store data in key-value pairs

student = {
    "name": "Lekhya",
    "age": 21
}

student["course"] = "Python"   # Add new key
print("After adding course:", student)

student["age"] = 22            # Update value
print("After updating age:", student)

student.pop("name")            # Remove key
print("After removing name:", student)

print("Keys:", student.keys())     # Get keys
print("Values:", student.values()) # Get values
print("Items:", student.items())   # Get key-value pairs
