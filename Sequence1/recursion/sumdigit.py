def sum_digit(n):
    if n < 10:
        return n

    return n % 10 + sum_digit(n // 10)

print(sum_digit(754321))