from stacklist import Stack

def validatePren(data):
  stack = Stack()
  opening = set('([{')
  closing = set(')]}')
  matches = {
		')' : '(',
		']' : '[',
		'}' : '{'
	}

  for i in data:
    if i in opening:
      stack.push(i)
    elif i in closing:
      last = stack.pop()
      if matches[i] != last:
        return False
    
  if stack.isEmpty():
    return True
  
  return False

data = '([{]])'
print(validatePren(data))