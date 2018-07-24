# python3
import sys


def PreprocessBWT(bwt):
  sorted_bwt = ''.join(sorted(bwt))
  dis_char = set(sorted_bwt)
  starts = {c: sorted_bwt.find(c) for c in dis_char}
  occ_counts_before = {}
  for c in dis_char:
    summary = [0]
    counter = 0
    for i in range(len(bwt)):
      if bwt[i] == c:
        counter += 1
      summary.append(counter)
    occ_counts_before[c] = summary
  print(starts, occ_counts_before)
  return (starts, occ_counts_before)


def CountOccurrences(pattern, bwt, starts, occ_counts_before):
  top = 0
  bottom = len(bwt) - 1
  while top <= bottom:
    if pattern:
      symbol = pattern[-1]
      pattern = pattern[:-1]
      if symbol in bwt[top: bottom + 1]:
        first_occurence = starts[symbol]
        top = first_occurence + occ_counts_before[symbol][top]
        bottom = first_occurence + occ_counts_before[symbol][bottom + 1] - 1
      else:
        return 0
    else:
      return bottom - top + 1
     


if __name__ == '__main__':
  bwt = sys.stdin.readline().strip()
  pattern_count = int(sys.stdin.readline().strip())
  patterns = sys.stdin.readline().strip().split()
  print(bwt, pattern_count, patterns)

  starts, occ_counts_before = PreprocessBWT(bwt)
  occurrence_counts = []
  for pattern in patterns:
    occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before))
  print(' '.join(map(str, occurrence_counts)))
