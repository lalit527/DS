def findMissing(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

    return arr1[-1]

arr1 = [5, 7, 8]
arr2 = [5,8]
print(findMissing(arr1, arr2))
