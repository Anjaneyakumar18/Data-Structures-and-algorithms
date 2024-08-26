#problem statement
'''
    An integer array is given then when ever you find the element
    that is bigger than the current element just put that bigger element in the
    current location

'''
    #1.Inplace
    #2.extra space


'''BRUTE FORCE ALGO WITH O(n**2)'''

# inplace used here
def next_greater_element(lst:list[int])->list[int]:
    for i in range(len(lst)):  #external loop i
        f=False
        for j in range(i,len(lst)): #internal loop j dependent on i loop 
            if lst[j]>lst[i]:
                lst[i]=lst[j]
                f=True
                break
        if not f:
            lst[i]=-1
arr=[1,4,2,6,7]
next_greater_element(arr)  #[4,6,6,7,-1]
print(arr)


#with out in place 
def with_out_inplace(lst:list[int])->list[int]:
    ans=[]
    for i in range(len(lst)):
        flag=False
        for j in range(i+1,len(lst)):
            if lst[j]>lst[i]:
                ans.append(lst[j])
                flag=True
                break
        if not flag:
            ans.append(-1)
    return ans



print(with_out_inplace([1,4,2,6,7]))



'''USING STACK TO MAKE IT O(n)'''


#approach
  
'''

     start traversing from back and use stack

'''

def next_greater_element_stack(arr: list[int]) -> list[int]:
    ans = []
    stack = []
    
    for i in range(len(arr) - 1, -1, -1):  
        while stack and stack[-1] <= arr[i]:  
            stack.pop()
        if stack:
            ans.append(stack[-1])  
        else:
            ans.append(-1)  
        stack.append(arr[i])  
    
    return ans[::-1]  

arr = [1, 4, 2, 6, 7]



print(next_greater_element_stack(arr))  


