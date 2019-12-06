length = 1
def collatz_conjecture(n):
    global length
    if n == 1:
        return length
    elif n % 2 == 1:
        length += 1
        collatz_conjecture(3*n+1)
    else: # n % 2 == 0
        length += 1
        collatz_conjecture(n/2)
    return length

print(collatz_conjecture(27))
