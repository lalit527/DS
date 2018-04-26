def sum(n):
    if n == 0:
        return 0
    
    result = n + sum(n - 1)

    return result

print(sum(4))