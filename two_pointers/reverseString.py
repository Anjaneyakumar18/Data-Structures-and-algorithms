def ReverseStr(s:str)->str:
    lst=list(s)
    i=0
    j=len(s)-1
    while i<j:
        lst[i],lst[j]=lst[j],lst[i]
        i+=1
        j-=1
    return ''.join(lst)

print(ReverseStr('abcedgh'))