# Python Functions - Beginner Friendly

# 1. Function without parameters and without return
def greet():
    # This function prints a message
    print("Hello, Welcome to Python")

greet()   # Function call

# 2. Function with parameters and without return
def show_sum(a, b):
    # Takes two values and prints their sum
    print("Sum:", a + b)

show_sum(10, 20)

# 3. Function without parameters and with return
def get_number():
    # Returns a value
    return 100

num = get_number()
print("Returned value:", num)

# 4. Function with parameters and with return
def add(a, b):
    # Takes two values and returns their sum
    return a + b

result = add(5, 6)
print("Addition result:", result)

# 5. Function with default parameter
def greet_user(name="User"):
    # If no value is passed, default value is used
    print("Hello", name)

greet_user()
greet_user("Lekhya")

# 6. Function with keyword arguments
def student_info(name, age):
    # Values passed using parameter names
    print("Name:", name)
    print("Age:", age)

student_info(age=21, name="Lekhya")

# 7. Function with variable length arguments (*args)
def add_numbers(*numbers):
    # Accepts multiple values
    total = 0
    for n in numbers:
        total += n
    print("Total:", total)

add_numbers(1, 2, 3, 4)

# 8. Function with variable length keyword arguments (**kwargs)
def student_details(**details):
    # Accepts key-value pairs
    for key, value in details.items():
        print(key, ":", value)

student_details(name="Lekhya", course="Python", year=3)

# 9. Lambda function (anonymous function)
square = lambda x: x * x   # One-line function
print("Square:", square(5))

# 10. Recursive function
def factorial(n):
    # Function calling itself
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))
