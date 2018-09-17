def bmw_matching(first_column, last_column, pattern, last_to_first):
  n = len(last_column)
  top = 0
  bottom = n - 1
  while top <= bottom:
    if pattern:
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

def preprocess_bwt(bwt):
  sorted_bwt = ''.join(sorted(bwt))
  print(sorted_bwt)
  dis_char = set(sorted_bwt)
  starts = {c: sorted_bwt.find(c) for c in dis_char}
  print(starts)
  occ_count_before = {}
  for c in dis_char:
    summary = [0]
    counter = 0
    for i in range(len(bwt)):
      if bwt[i] == c:
        counter += 1
      summary.append(counter)
    occ_count_before[c] = summary
  print(occ_count_before)
  return starts, occ_count_before


def count_occurrences(pattern, bwt, starts, occ_count_before):
  top = 0
  bottom = len(bwt) - 1
  while top <= bottom:
    if pattern:
      symbol = pattern[-1]
      pattern = pattern[:-1]
      if symbol in bwt[top: bottom + 1]:
        first_occurence = starts[symbol]
        top = first_occurence + occ_count_before[symbol][top]
        bottom = first_occurence + occ_count_before[symbol][bottom + 1] - 1
      else:
        return 0
    else:
      return bottom - top + 1



if __name__ == "__main__":
  bwt = "ATT$AA"
  pattern = "ATA"
  starts, occ_count_before = preprocess_bwt(bwt)
  print(count_occurrences(pattern, bwt, starts, occ_count_before))