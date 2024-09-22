def KthSymbol(s,n,k):
    if n==0:
        return s[k-1]
    ret=''
    for ch in s:
        if ch=='0':
            ret+='10'
        else:
            ret+='01'
    return KthSymbol(ret,n-1,k)

print(KthSymbol('0',4,3))