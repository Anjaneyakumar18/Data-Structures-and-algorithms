def deletemiddle(stack1,stack2):
    if len(stack1)==len(stack2) or len(stack1)-len(stack2)==1:
        stack1.pop()
        while stack2:
            stack1.append(stack2.pop())
        return stack1
    
    stack2.append(stack1.pop())

    return deletemiddle(stack1,stack2)

print(deletemiddle([2,5,6,7,6],[]))


def stackMidDel(n,i):
    if n//2==i:
        return stack.pop(i)
    i-=1
    return stackMidDel(n,i)
stack=[1,2,3,4,5,6]
n=len(stack)
print(stackMidDel(n,n))