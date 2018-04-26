def coinChange(value, changes):
    if value == 0:
        return 1
    
    if value < 0:
        return 0

    combination += coinChange(value, changes[])

    return combination

changes = [1, 2, 3]
value = 4
print(coinChange(value, changes))