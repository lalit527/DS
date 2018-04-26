def coin_change(value, changes):
    min_coins = value

    if value in changes:
        return 1
    else:
        for i in [c for c in changes if c <= value]:
            num_coins = 1 + coin_change(value - i, changes)

        if num_coins < min_coins:
            min_coins = num_coins

    return min_coins

def coin_change_dyn(value, changes, results):
    min_coins = value

    if value in changes:
        results[value] = 1
        return 1
    elif results[value] > 0:
        return results[value]

    else:
        for i in [c for c in changes if c <= value]:
            num_coins = 1 + coin_change_dyn(value - i, changes, results)

        if num_coins < min_coins:
            min_coins = num_coins

            results[value] = min_coins

    return min_coins


changes = [1,5,10,25]
value = 63
known_results = [0]*(value+1)
print(coin_change_dyn(value, changes, known_results))