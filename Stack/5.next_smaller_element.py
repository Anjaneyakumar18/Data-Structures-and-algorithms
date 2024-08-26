#BRUTE FORCE 0(N**2)


#inplace solution

def nearest_right_smaller_element_inplace(arr:list[int])->list[int]:
    for i in range(len(arr)):
        flag=True
        for j in range(i,len(arr)):
            if arr[j]<arr[i]:
                arr[i]=arr[j]
                flag=False
                break
        if flag:
            arr[i]=-1
    return arr
print(nearest_right_smaller_element_inplace([2,4,1,6,7,3]))  

#extra space solution

def nearest_right_smaller_element(arr:list[int])->list[int]:
    ans=[]
    for i in range(len(arr)):
        flag=True
        for j in range(i,len(arr)):
            if arr[j]<arr[i]:
                ans.append(arr[j])
                flag=False
                break
        if flag:
            ans.append(-1)
    return ans
print(nearest_right_smaller_element([2,4,1,6,7,3]))


#using stack solution O(n)

def stack_solution(lst:list[int])->list[int]:
    ans=[]
    stack=[]
    for i in range(len(lst)-1,-1,-1):
        while stack and stack[-1]>=lst[i]:
            stack.pop()
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)
        stack.append(lst[i])
    return ans[::-1]


print(stack_solution([2,4,1,6,7,3]))