# w2 : Python (text mode)
# print, input, escape sequence, f-string, user-defined function

def show_info():
    print("This program will calculate area of a land")
    print("given width and length")
    print()
    print("created by <student name>")

def get_width():
    return float(input("Enter width (m): "))

def get_length():
    return float(input("Enter length (m): "))

def cal_area(width, length):
    return width * length

def show_area(area):
    print("The result area is", area, "(in square meter)")

def show_area_in_SqWa(area):
    print("The result area is", area / 4, "(in square wa)")

name = "Alice"
print(f"Hello, {name}!")
print("Hello, {}!!!".format(name))
print("Welcome to \nPython3.14 \n\tPython2.7")  # \n new line, \t tab

show_info()
width = get_width()
length = get_length()
area = cal_area(width, length)
show_area(area)
show_area_in_SqWa(area)
