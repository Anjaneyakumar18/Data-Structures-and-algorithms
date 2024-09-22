def sorting(arr):
    print(arr)
    if len(arr) <= 1:
        
        return arr
    
    lst = sorting(arr[:-1])
    
    return binding(lst, arr[-1])

def binding(lst, ele):
    for i in range(len(lst)):
        if ele < lst[i]:
            print(lst)
            lst.insert(i, ele)
            return lst
    print(lst)
    lst.append(ele)
    return lst

print(sorting([1, 5, 6, 3]))  
