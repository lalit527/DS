def missingTwo(arr):
    n = len(arr) + 2
    XOR = arr[0]
    for i in range(1, n-2):
        XOR ^= arr[i]
    for i in range(1, n+1):
        XOR ^= i

    set_right_bit = XOR & ~(XOR - 1)

    x = 0
    y = 0

    for i in range(0, n-2):
        if arr[i] & set_right_bit:
            x ^= arr[i]
        else:
            y ^= arr[i]

    for i in range(1, n+1):
        if i & set_right_bit:
            x ^= i
        else:
            y ^= i

    print(x,y)

arr = [2, 5, 3, 4, 1, 7, 9]
print(missingTwo(arr))