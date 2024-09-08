def twosum(arr,target):
    
    index={}
    for i in range(len(arr)):
        if target-arr[i] in index:
            return [index[target-arr[i]],i]
        index[arr[i]]=i
    return [-1,-1]

arr=[1,8,5,3,9,3,2]

print(twosum(arr,12))