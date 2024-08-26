def valid_brackets(s: str) -> bool:
    table = {')': '(', '}': '{', ']': '['}
    stack = []
    

    for ch in s:
        if not stack and ch in table.keys():
            return False
        elif stack and ch in table.keys():
            if stack[-1] == table[ch]:  
                stack.pop()
            else:
                return False
        else:
            stack.append(ch)
    
    
    return not stack  

print(valid_brackets("{[()]}"))  
