# w5 : Python (text mode)
# function with return value, main(), array (list) : print, sum, average, max

def sum_1_to_n(n):
    sum = 0
    count = 1
    while count <= n:
        sum = sum + count
        count = count + 1
    return sum

def main():  # do not need global variables
    n = 5
    print("Sum from 1 to", n, "=", sum_1_to_n(n))
    n = 10
    print("Sum from 1 to", n, "=", sum_1_to_n(n))

    a = [5, 9, 2]  # index start from 0 (up to 2)

    # print elements of array
    i = 0
    while i < len(a):  # len(a) is length of a
        print("a[", i, "] = ", a[i])
        i = i + 1

    # sum and average
    sum = 0
    i = 0
    while i < len(a):
        sum = sum + a[i]
        i = i + 1
    print("Sum =", sum)
    print("Average =", sum / len(a))

    # maximum value
    max = a[0]
    i = 1
    while i < len(a):
        if max < a[i]:
            max = a[i]
        i = i + 1
    print("Max =", max)

if __name__ == "__main__":
    main()
