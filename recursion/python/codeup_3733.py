# 아직 통과는 못 함...

length = 1
def f(min_max):
    [a, b] = [int(x) for x in min_max.split()]

    def g(n):
        global length
        if n == 1:
            return length
        elif n % 2 == 1:
            length += 1
            g(3*n+1)
        else:
            length += 1
            g(n/2)
        result = length
        return result

    longest = 1
    longest_length = 1
    for i in range(a, b):
        global length
        length = 1
        if g(i) > longest_length:
            length = 1
            longest = i
            longest_length = g(i)

    return f'{longest} {longest_length}'

print(f(input()))
