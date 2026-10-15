# w10 : Python (text mode)
# function and array, pass by value / reference, 2D array, nested loop, matrix

def print_all(a):
    i = 0
    while i < len(a):
        print(a[i])
        i = i + 1

def add_all(a, x):  # array : can change its elements
    i = 0
    while i < len(a):
        a[i] = a[i] + x
        i = i + 1

def add_x(a, x):  # number : value is copied (pass by value)
    a = a + x

def print_2Dn(m):
    i = 0
    while i < len(m):  # outer loop
        j = 0
        while j < len(m[i]):  # inner (nested) loop
            print(m[i][j], end=" ")
            j = j + 1
        print()
        i = i + 1

def sum_2Dn(m):
    sum = 0
    i = 0
    while i < len(m):
        j = 0
        while j < len(m[i]):
            sum = sum + m[i][j]
            j = j + 1
        i = i + 1
    return sum

def count_2Dn(m, x):
    count = 0
    i = 0
    while i < len(m):
        j = 0
        while j < len(m[i]):
            if m[i][j] == x:
                count = count + 1
            j = j + 1
        i = i + 1
    return count

def addm(A, B):  # add 2 matrices
    result = []
    i = 0
    while i < len(A):  # loop every row
        row = []
        j = 0
        while j < len(A[i]):  # loop every column
            row.append(A[i][j] + B[i][j])
            j = j + 1
        result.append(row)
        i = i + 1
    return result

a = [5, 9, 2]
add_all(a, 3)
print_all(a)  # 8 12 5

b = 2
add_x(b, 7)
print(b)  # 2 (b is unchanged)

# 2D array (list of lists), use 2 indexes (row, col)
m = [[5, 7, 9],
     [2, 4, 6],
     [8, 3, 1]]
print(m[0][0], m[0][1], m[1][0])  # 5 7 2
m[1][2] = 7
m[2][2] = 5
print_2Dn(m)
print("Sum =", sum_2Dn(m))
print("Count of 7 =", count_2Dn(m, 7))

A = [[1, 2],
     [3, 4]]
B = [[5, 6],
     [7, 8]]
print(addm(A, B))  # [[6, 8], [10, 12]]
