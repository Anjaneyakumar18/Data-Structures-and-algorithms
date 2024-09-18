'''
 |
 |   |     |
 | | |     |
 | | | | | |
 | | | | | |
 | | | | | |


'''
def maxAreaContiner(arr:list[int])->int:
    i=0
    j=len(arr)-1
    max_area=0
    while j>=i:
        max_area=max(max_area,min(arr[i],arr[j])*(j-i))
        if arr[i]>arr[j]:
            j-=1
        else:
            i+=1
    return max_area

arr=[6,4,5,3,3,5]

result=maxAreaContiner(arr)

print(result)