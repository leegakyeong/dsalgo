memo = {}
def triangle(r, c):
    if r == 1 or c == 1:
        return 1
    elif (r,c) in memo.keys():
        return memo[(r,c)]
    result = triangle(r-1, c) + triangle(r, c-1)
    memo[(r,c)] = result
    return result % 100000000

r, c = [int(i) for i in input().split(' ')]
print(triangle(r, c))
