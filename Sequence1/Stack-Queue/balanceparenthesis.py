def balanceParen(s):
	if len(s) == 0:
		return True
	stack = []
	opening = set('([{')
	closing = set(')]}')
	matches = {
		'(' : ')',
		'[' : ']',
		'{' : '}'
	}

	for i in s:
		if i in opening:
			stack.append(i)
		elif i in closing:
			last = stack.pop()
			if matches[last] != i:
				return False
	if len(stack) == 0:
		return True

	return False