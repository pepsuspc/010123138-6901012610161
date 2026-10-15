# w4 : Python (text mode)
# if / else, nested if, while loop, random, password
import random
import getpass

# Nested conditional statement
x = random.randint(-5, 5)
print("x =", x)
if x > 0:
    print("x is positive")
else:
    if x < 0:
        print("x is negative")
    else:
        print("x is zero")

# while statement
n = 5             # initialise
while n > 0:      # condition
    print(n)
    n = n - 1     # update (do not forget, or infinite loop)

# print a line of n stars
def print_line(n):
    while n > 0:
        print("*", end="")  # do not add a newline
        n = n - 1
    print()  # add a newline

print_line(5)

# Loop until -1 is entered
sum = 0
num = int(input("Enter a number (-1 to stop): "))
while num != -1:
    sum = sum + num
    num = int(input("Enter a number (-1 to stop): "))
print("Sum =", sum)

# Password : limit number of tries
count = 0
granted = False
while count < 3 and not granted:
    user_password = getpass.getpass("Enter your password: ")  # not show it
    if user_password == "secret123":
        print("Access granted :)")
        granted = True
    else:
        print("Access denied!")
    count = count + 1
