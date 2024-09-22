def poweroffour(n):
    if n==1:
        return True
    elif n%4!=0 or n<=0:
        return False
    return poweroffour(n//4)

print(poweroffour(16))