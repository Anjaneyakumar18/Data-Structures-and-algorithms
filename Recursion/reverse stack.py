def reverseStack(stack):
    if not stack:
        return 
    
    k=stack.pop()
    reverseStack(stack)
    stack.insert(0,k)   #pushbottom

    return stack

stack=[1,2,3,4,5]

res=reverseStack(stack)

print(res)