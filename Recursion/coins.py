def coins(arr,comb,total):
    if sum(comb)==total:
        ans.append(comb.copy())
    for i in range(len(arr)):
        comb.append(arr[i])
        coins(arr[i+1:],comb,total)
        comb.pop()
arr=[1,2,3,5,6,7,8,9,10]
ans=[]
coins(arr,[],12)
print(ans)