# python3

from sys import stdin
import copy as cp
import numpy as np

NO_SOL = "No solution"
BOUNDED = "Bounded solution"
INF = "Infinity"
BIG = 1e9
SMALL = float('-Infinity')
EPS = 0.0003

def ReadEquation():
    n, m = list(map(int, stdin.readline().split()))
    A = []
    for i in range(n):
      A += [list(map(int, stdin.readline().split()))]
    b = list(map(int, stdin.readline().split()))
    c = list(map(int, stdin.readline().split()))
    return n, m, A, b, c

def add_equations(n, m, A, b):
    for i in range(m):
        e = [0.0] * m
        e[i] = -1.0
        A.append(e)
        b.append(0.0)
    A.append([1.0] * m)
    b.append(BIG)

def solve_diet_problem(n, m, A, b, c):
    add_equations(n, m, A, b)
    l = n + m + 1
    ans = -1
    score = float('-inf')
    result = None
    for i in range(l ** 2):
        index = [i for i in range(l) if ((x / 2 ** i) % 2) // 1 == 1]
        if len(index) != m:
            continue
        last_eq = False
        if index[-1] == l - 1:
            last_eq = True
        

if __name__ == '__main__':
    n, m, A, b, c = ReadEquation()
    s = solve_diet_problem(n, m, A, b, c)
    print(s[0])
    print(" ".join(s[1]))