def f(n):
    for i in range(1, n+1):
        for j in range(0, n):
            print(i*n-j, end=' ')
    print()

f(int(input()))
