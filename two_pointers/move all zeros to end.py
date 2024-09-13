def moveZeros(arr:list[int])->list[int]:
    left,right=0,len(arr)-1

    while left<right:
        if arr[left]==0:
            arr[left],arr[right]=arr[right],arr[left]
            right-=1
        if arr[left]!=0:
            left+=1
    return arr
    
print(moveZeros([8,5,0,8,3,4,6,0,2,1,0,8,6,5,0,0,0,2,3,4,5,0]))