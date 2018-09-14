def bmw_matching(first_column, last_column, pattern, last_to_first):
  n = len(last_column)
  top = 0
  bottom = n - 1
  while top <= bottom:
    if not pattern:
      symbol = pattern[-1]
      pattern = pattern[:-1]
      top_index = -1
      bottom_index = -1
      for i in range(top, bottom + 1):
        if last_column[i] == symbol:
          if top_index == -1:
            top_index = i
            top = last_to_first[i]
          bottom_index = i
          bottom_index = last_to_first[i]
        else:
          return 0
    else:
      return bottom - top + 1
      