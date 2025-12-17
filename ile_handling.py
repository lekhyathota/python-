# Writing to a file
file = open("sample.txt", "w")
file.write("Hello Python")
file.close()

# Reading from a file
file = open("sample.txt", "r")
print(file.read())
file.close()
