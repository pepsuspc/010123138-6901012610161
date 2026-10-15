# w7 : Python (text mode)
# factorial (loop / recursive), file : write, append, read, try-except

def factorial_loop(n):
    result = 1
    i = 1
    while i <= n:
        result = result * i
        i = i + 1
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

print("5! =", factorial_loop(5))
print("5! =", factorial_recursive(5))

# Write to file ("w") - must add newline (\n) manually
with open("example.txt", "w") as file:
    file.write("5\n")
    file.write("2\n")
    file.write("7\n")

with open("output.txt", "w") as file:
    file.write("Hello Python\n")
    file.write("Welcome to Thailand\n")

# Append to file ("a") - add to the end of file
with open("output.txt", "a") as file:
    file.write("ECE\n")
    file.write("KMUTNB\n")

# Read the entire content (file will be closed automatically)
with open("output.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line, while the line is not empty (not EOF)
with open("output.txt", "r") as f:
    line = f.readline()
    while line:
        print(line, end="")
        line = f.readline()

# Process line by line -> array
a = []
with open("example.txt", "r") as file:
    for line in file:
        num = int(line)  # convert to int
        a.append(num)
print(a)  # [5, 2, 7]

# File not found -> try and catch exception
try:
    with open("not_found.txt", "r") as f:
        for line in f:
            print(line)
except FileNotFoundError:
    print("Error: not_found.txt is not found")
