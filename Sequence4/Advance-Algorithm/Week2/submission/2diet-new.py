# python3

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

def subset(s, f):
    def powerset(iterable):
        s = list(iterable)
        res = chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))
        return res
    return filter(lambda x: len(x) == f, map(set, powerset(s)))    

def gauss(A):
    n = len(A)
    for i in range(n):
        max_el = abs(A[i][i])
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i] > max_el):
                max_el = abs(A[k][i])
                max_row = k
        if A[max_row][i] == 0:
            return False, []
        
        for k in range(i, n + 1):
            tmp = A[max_row][k]
            A[max_row][k] = A[i][k]
            A[i][k] = tmp
        for k in range(i + 1, n):
            c =-A[k][i]/ A[i][i]
            for j in range(i, n + 1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]
    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = A[i][n] / A[i][i]
        for k in range(i - 1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    return True, x


def to_str(x):
    return list(map(lambda a : '%.18f' % a, x))

def check_sol(sol, A, sub_set_indx):
    rowL = len(A[0])
    idx = [i for i in range(len(A)) if i not in sub_set_indx]
    for i in idx:
        sub_sol = 0
        for j in range(rowL - 1):
            sub_sol += A[i][j] * sol[j]
        if (sub_sol > A[i][rowL - 1] * EPS):
            return False
    return True

def simplex(A, c):
    sol = []
    n = len(A)
    m = len(A[0]) - 1
    t = NO_SOL
    obj = SMALL
    if m > n:
        return INF, []
    for eq in subset(range(n), m):
        subA = [A[i] for i in eq]
        has_sol, sol_subA = gauss(subA)
        if has_sol and check_sol(sol_subA, A, eq):
            local_max = 0
            for i in range(len(sol_subA)):
                local_max += sol_subA[i] * c[i]
            if local_max > obj:
                obj = local_max
                sol = sol_subA
            is_bounded = True
            if n - 1 in subA:
                is_bounded = False
    if obj != SMALL:
        t = INF
        if is_bounded:
            t = BOUNDED
    return t, to_str(sol)


if __name__ == '__main__':
    equation, pleasure = ReadEquation()
    s = simplex(equation, pleasure)
    print(s[0])
    print(" ".join(s[1]))