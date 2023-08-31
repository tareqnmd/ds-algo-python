def recursive(n):
    if n == 1:
        print(1)
    else:
        print(n)
        recursive(n - 1)
        print(n)


recursive(10)
