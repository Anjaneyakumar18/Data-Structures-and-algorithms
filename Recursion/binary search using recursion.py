def binarysearch(low,high,searchkey,arr):
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid]==searchkey:
        return mid
    elif arr[mid]>searchkey:
        return binarysearch(low,mid-1,searchkey,arr)
    else:
        return binarysearch(mid+1,high,searchkey,arr)
arr=[1,2,3,4,5,6,7,8,9,10]
print(binarysearch(0,len(arr)-1,6,arr))