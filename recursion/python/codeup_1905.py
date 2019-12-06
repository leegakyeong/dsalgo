import sys
sys.setrecursionlimit(99999)

def sum(n):
    if n == 1:
        return n
    else:
        return n + sum(n-1)

i = int(input())
print(sum(i))
