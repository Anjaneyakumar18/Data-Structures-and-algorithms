def nearest_left_smaller_element(arr:list[int])->list[int]:
    ans=[]
    for i in range(len(arr)-1,-1,-1):
        flag=True
        for j in range(i,-1,-1):
            if arr[j]<arr[i]:
                ans.append(arr[j])
                flag=False
                break
        if flag:
            ans.append(-1)
    return ans[::-1]
print(nearest_left_smaller_element([10,3,7,8,1,4]))



#using stack



def stack_solution(arr:list[int])->list[int]:
    ans=[]
    stack=[]
    for i in range(len(arr)):
        while stack and stack[-1]>=arr[i]:
            stack.pop()
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)
        stack.append(arr[i])
    return ans
print(stack_solution([10,3,7,8,1,4]))