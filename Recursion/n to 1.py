def rec(n):
    if n==0:
        return
    print(n)
    rec(n-1)

rec(10)