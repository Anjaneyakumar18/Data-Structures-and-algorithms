def convert(s:str)->str:
    stack=[]
    s=s[::-1]
    operators={'+':1,'-':1,'*':2,'/':2,'^':3}
    ans=''
    for ch in s:
        if ch.isalpha():
            ans+=ch
        elif ch in operators:
            if not stack:
                stack.append(ch)
            else:
                while stack and operators[stack[-1]]>operators[ch]:
                    ans+=stack.pop()
                stack.append(ch)
    while stack:
        ans+=stack.pop()
    return ans[::-1]


print(convert('a+b+c^d*f+k'))
