def f(a, b):
    k = int(a)
    arr = b.split()
    for i in range(k):
        print(' '.join(arr))
        arr.insert(k, arr.pop(0))

f(input(), input())
