def poweroftwo(n):
    if n==1:
        return True
    elif n%2!=0 or n<=0:
        return False
    return poweroftwo(n//2)

print(poweroftwo(2048))