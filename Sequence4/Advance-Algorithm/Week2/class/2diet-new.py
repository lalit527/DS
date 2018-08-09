from sys import stdin
from itertools import chain, combinations

NO_SOL = "No solution"
BOUNDED = "Bounded solution"
INF = "Infinity"
BIG = 10000000000
SMALL = float('-Infinity')
EPS = 0.0003

def ReadEquation():
    n, m = list(map(int, stdin.readline().split()))
    A = []
    for i in range(n):
      A += [list(map(int, stdin.readline().split()))]
    b = list(map(int, stdin.readline().split()))
    for i in range(len(A)):
      A[i].append(b[i])
    c = list(map(int, stdin.readline().split()))
    return A, c

def subset(n, m):
    def power

def simplex(A, c):
    sol = []
    n = len(A)
    m = len(A[0]) - 1
    t = NO_SOL
    obj = SMALL
    if m > n:
        return INF, []
    for eq in subset(range(n), m):
        pass

if __name__ == '__main__':
    equation, pleasure = ReadEquation()
    s = simplex(equation, pleasure)
    print(s)
    tmp = ""
    for i in s[1]:
        tmp += i + " "
    print(tmp[:-1])