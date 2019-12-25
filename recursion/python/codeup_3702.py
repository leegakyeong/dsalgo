memo = {}
def triangle(r, c):
    if r == 1 or c == 1:
        return 1
    elif memo.get((r,c)):
        return memo[(r,c)]
    else:
        result = triangle(r-1, c) + triangle(r, c-1)
        memo[(r,c)] = result
        return result % 100000000

r, c = [int(i) for i in input().split(' ')]
print(triangle(r, c))
