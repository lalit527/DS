def min_edit_distance(str1, str2):
	n = len(str1)
	m = len(str2)
	return _min_edit_distance(str1, str2, n, m)

def _min_edit_distance(str1, str2, n, m):
	if n == 0:
		return m
	if m == 0:
		return n
	if str1[n - 1] == str2[m - 1]:
		return _min_edit_distance(str1, str2, n - 1, m - 1)
	return min(_min_edit_distance(str1, str2, n - 1, m), _min_edit_distance(str1, str2, n, m - 1), _min_edit_distance(str1, str2, n - 1, m - 1)) + 1

if __name__ == '__main__':
    str1 = "azced"
    str2 = "abcdef"
    print(min_edit_distance(str1, str2))
