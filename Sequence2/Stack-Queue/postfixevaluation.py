from stacklist import Stack

def isOperand(c):
  try:
    float(c)
    return True
  except:
    return False

def eval_postfix(exp):
  n = len(exp)
  if n < 1:
    return None
  stack = Stack()
  for i in range(n):
    if isOperand(exp[i]):
      stack.push(exp[i])
    else:
      ele1 = stack.pop()
      ele2 = stack.pop()
      print(ele1, ele2, exp[i])
      n = eval(ele2 + exp[i] + ele1)
      stack.push(str(int(n)))

  result = stack.pop()
  return result

exp = '231*+9-'
print(eval_postfix(exp))