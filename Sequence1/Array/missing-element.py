##############################################
# Operation 1: finding missing element ##
##############################################
def findMissing(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

    return arr1[-1]



##############################################
# Operation 2: finding missing element
# using dictonary ##
##############################################
# finding the missing element
from collections import defaultdict
def findMissing2(arr1, arr2):
    d = defaultdict(int)
    for num in arr2:
        d[num] += 1
    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1


##############################################
# Operation 2: finding missing element
# using XOR operation ##
##############################################

def findMissingXOR(arr1, arr2):
    result = 0
    for num in arr1 + arr2:
        print("num", num)
        result ^= num
        print("result", result)

    return result

arr1 = [5, 7, 8]
arr2 = [5,8]
print("The missing element is", findMissingXOR(arr1, arr2))




