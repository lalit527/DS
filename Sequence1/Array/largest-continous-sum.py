##############################################
# Operation 1: finding largest sum ##
##############################################
def largestContinousSum(arr):
    if len(arr) == 0:
        return 0
    current_sum = max_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

    return max_sum

##############################################
# Operation 2: finding largest sum ##
##############################################
def largestContinousSum2(arr):
    if len(arr) == 0:
        return 0
    max_so_far = 0
    max_ending_here = 0
    start = 0
    end = 0

    for num in arr:
        max_ending_here = max_ending_here + num
        if max_ending_here < 0:
            max_ending_here = 0
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
    print(max_ending_here)
    return max_so_far

##############################################
# Operation 2: finding largest sum with start
# and end index##
##############################################
def largestContinousSum3(arr):
    if len(arr) == 0:
        return 0
    max_so_far = 0
    max_ending_here = 0
    start = 0
    end = 0
    s = 0

    for index in range(len(arr)):
        max_ending_here = max_ending_here + arr[index]
        if max_ending_here < 0:
            max_ending_here = 0
            s = index + 1
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = index
    print("Maximum contiguous sum is", max_so_far)
    print("Starting Index", start)
    print("Ending Index", end)
    print(max_ending_here)
    return max_so_far



arr = [1, 5, 7, -10, 2, 9, 5, 6]
#a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(largestContinousSum3(arr))


