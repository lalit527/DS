def grouping_children(children):
  children.sort()
  R = 1
  i = 1
  n = len(children)
  while i < n - 1:
    l, r = children[i], children[i + 1]
    R += 1
    i = i + 1
    while i < n and children[i] <= r:
      i = i + 1
  return R

print(grouping_children([8, 17, 18, 9, 3, 2, 1]))


