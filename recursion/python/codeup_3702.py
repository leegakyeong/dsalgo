def triangle(r, c):
    if r == 1 or c == 1:
        return 1
    else:
        return triangle(r-1, c) + triangle(r, c-1)

print(triangle(3, 2))
