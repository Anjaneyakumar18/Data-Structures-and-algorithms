def sortstack(stack:list[int])->list[int]:

    if len(stack)==1:
        return stack
    
    k=stack.pop()

    lst=sortstack(stack)

    return binding(lst,k)

def binding(lst,k):
    for i in range(len(lst)):
        if lst[i]>=k:
            lst.insert(i,k)
            return lst
    lst.append(k)
    return lst

print(sortstack([6,3,0,9]))