def longest_common(sequence):
	n = len(sequence)
	longest = 0
	for i in range(n):
		current = _longest_common(sequence, i + 1, sequence[i])
		if current > longest:
			longest = current	
	return longest + 1

def _longest_common(sequence, next_index, current):
	if next_index == len(sequence):
		return 0
	temp1 = 0
	if current < sequence[next_index]:
		temp1 = 1 + _longest_common(sequence, next_index + 1, sequence[next_index])
	temp2 = _longest_common(sequence, next_index + 1, current)
	return max(temp1, temp2)

####################################################################
#DP 
def longest_common_dp(sequence):
	n = len(sequence)
	T = [1 for _ in range(n)]
	for i in range(n):
		for j in range(i):
			if sequence[i] > sequence[j]:
				T[i] = 1 + T[j]
	return max(T)

sequence = [23, 10, 22, 5, 33, 8, 9, 21, 50, 41, 60, 80, 99, 22, 23, 24, 25, 26, 27]
print(longest_common_dp(sequence))


"""
def longest_subsequence(sequence):
  n = len(sequence)
  max_len = 0
  for i in range(1, n):
    cur_max = _longest_subsequence(sequence, i + 1, sequence[i])
    if cur_max > max_len:
       max_len = cur_max
  return max_len + 1

def _longest_subsequence(sequence, next_index, current):
  if next_index == len(sequence):
    return 0
  temp1 = 0
  if sequence[next_index] > current:
    return 1 + _longest_subsequence(sequence, next_index + 1, sequence[next_index])
  temp2 =  _longest_subsequence(sequence, next_index + 1, current)
  return min(temp1, temp2)


def longest_sequence_dp(sequence):
  n = len(sequence)
  T = [1 for _ in range(n)]
  for i in range(n):
    for j in range(i):
      if sequence[i] > sequence[j]:
        T[i] = 1 + T[j]
  return max(T)
"""