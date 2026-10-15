# w6 : Python (text mode)
# sum m to n, is_sorted, string : ASCII, escape, concatenation, immutable, methods

def sum_m_to_n(m, n):
    sum = 0
    count = m
    while count <= n:
        sum = sum + count
        count = count + 1
    return sum

def is_sorted(a):
    i = 0
    while i < (len(a) - 1):
        if a[i] > a[i + 1]:
            return False
        i = i + 1
    return True

print("Sum from 3 to 7 =", sum_m_to_n(3, 7))
print([5, 9, 2], "is sorted?", is_sorted([5, 9, 2]))
print([2, 5, 9], "is sorted?", is_sorted([2, 5, 9]))

# String : similar to array of characters
s = "Hello"
i = 0
while i < len(s):
    print(s[i], ord(s[i]))  # character and its ASCII code
    i = i + 1
print(chr(97), chr(65))  # a A  (reverse of ord())

# Escape characters
print("Hello\nWorld")
print("Python\tProgramming")
print("He said \"Hello\"")

# String concatenation ( + )
t = ""
i = 0
while i < len(s):
    t = t + str(i) + "\t" + s[i] + "\n"  # str() converts integer to string
    i = i + 1
print(t)

# String is immutable -> create a new string instead
# s[0] = "J"  # TypeError: 'str' object does not support item assignment
s = "J" + s[4] + s[1]
print(s)  # Joe

# String methods
print("Hello".upper(), "Hello".lower())
print("A".isalpha(), "3".isdigit(), "3".isalnum())
