def valid(s:str)->bool:
    stack=[]
    for ch in s:
        if not stack and ch==')':
            return False
        elif stack and ch==')':
            if stack[-1]=='(':
                stack.pop()
            else:
                return False
        else:
            stack.append(ch)
    return not bool(stack)
print(valid('((()))'))