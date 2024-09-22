def subsets(arr,comb):
    ans.append(comb.copy())
    for i in range(len(arr)):
        comb.append(arr[i])
        subsets(arr[i+1:],comb)
        comb.pop()
    return 

ans=[]
arr=[1,2]
comb=[]
subsets(arr,comb)
print(ans)