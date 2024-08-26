def conver(s:str)->str:
    operators={'+':1,'-':1,'*':2,'/':2,'^':3}
    stack=[]
    ans=''
    for ch in s[::-1]:
        if not stack and ch in operators.keys():
            stack.append(ch)
        elif ch.isalpha():
            ans+=ch
        else:
            while stack and operators[stack[-1]]>operators[ch]:
                ans+=(stack.pop())
            stack.append(ch)
    while stack:
        ans+=stack.pop()
    
    return ans


print(conver('a+b+c*d/g'))
