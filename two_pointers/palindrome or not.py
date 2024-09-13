def palindrome(s:str)->bool:
    i=0
    j=len(s)-1
    while i<j:
        if s[i]==s[j]:
            i+=1
            j-=1
        else:
            return False
    return True

print(palindrome('abcaba'))