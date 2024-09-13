"""
"abcdef" --> "ebcdaf"

"""

def swap_vowels(s:str)->str:
    word=list(s)
    i,j=0,len(s)-1
    vowels='aeiouAEIOU'
    while j>i:
        if (word[i] in vowels) and (word[j] in vowels):
            word[i],word[j]=word[j],word[i]
            i+=1
            j-=1
        elif word[i] in vowels:
            j-=1
        elif word[j] in vowels:
            i+=1
        else:
            i+=1
            j-=1
    return ''.join(word)