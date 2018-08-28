# uses python3

from collections import defaultdict
import itertools

binary = int(input())
position = binary - 1

last = '1' * binary
bin_int = int(last, 2)

last_before = "1" + ('0'*position)
first = '0'*binary
nodes = defaultdict(list)
for i in range(bin_int + 1):
  m = (bin(i)[2:].zfill(binary))
  if m != last_before and m != first:
    s = m[0:position]
    edge = m[1:binary]
    nodes[s].append(edge)
    nodes[edge].append(s)

start = '0' * (binary - 1)
tour = [start]
current = start
while len(nodes[current]) > 0:
  suffix = current[1:]
  next_char = "1" if suffix + "1" in nodes[current] else "0"
  tour.append(suffix + next_char)
  nodes[current].remove(suffix + next_char)
  nodes[suffix + next_char].remove(current)
  current = suffix + next_char

res = '0'
for i, d in enumerate(tour):
  res += d[0]
print(res)