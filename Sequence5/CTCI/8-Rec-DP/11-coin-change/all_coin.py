def make_change(amount, denom):
  result = []
  count = [0]
  _make_change(amount, denom, 0, len(denom), result, count)
  return count[0]

def _make_change(amount, denom, index, end, result, count):
  if amount == 0:
    print(result, count)
    count[0] += 1
  else:
    for i in range(index, end):
      if denom[i] <= amount:
        result.append(denom[i])
        _make_change(amount - denom[i], denom, i, end, result, count)
        result.pop()


def make_change_count(amount, denom):
  count = [0]
  _make_change_count(amount, denom, 0, len(denom), count)
  return count[0]

def _make_change_count(amount, denom, index, end, count):
  if amount == 0:
    count[0] += 1
  else:
    for i in range(index, end):
      if denom[i] <= amount:
        _make_change_count(amount - denom[i], denom, i, end, count)


def min_change_count(amount, denom):
  if amount <= 0:
    return 0
  min_val = float('inf')
  for i in denom:
    min_val = min(min_val, 1 + min_change_count(amount - i, denom))
  return min_val

if __name__ == "__main__":
  amount = 8
  change = [1, 2, 3, 4]
  print(make_change(amount, change))