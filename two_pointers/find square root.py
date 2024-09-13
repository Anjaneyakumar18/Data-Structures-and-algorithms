def squareNum(n: int) -> float:
    l = 0
    r = n
    while r>l:
        mid = (l + r) / 2  
        if mid * mid == n:
            return mid
        elif mid * mid > n:
            r = mid
        else:
            l = mid
    
    return (l + r) / 2  

print(squareNum(81))