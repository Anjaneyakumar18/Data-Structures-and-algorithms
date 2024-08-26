## Largest area histogram Leetcode - ###

'''
     4     4 4  
     _     _ _   3
    | |2  | | |  _
    | |_ 1| | |1| |
    | | |_| | |_| |
   _|_|_|_|_|_|_|_|_

   as the above fig the heigts of  the bildings are given each building is know as histogram 
   find the maximum area that collecation of histograms can form 
   in the above fiv 8 is max ((index 3 and 4 ))

'''



def Largest_area_histogram(arr:list[int])->int:
    stack1=[]
    stack2=[]
    left=[]
    right=[]
    histo=0

    # finding right smallest element of each ele

    for i in range(len(arr)):
        while stack1 and stack1[-1][0]>=arr[i]:
            stack1.pop()
        if not stack1:
            left.append(-1)
        else:
            left.append(stack1[-1][1])
        stack1.append((arr[i],i))

    # finding the right smallest element of each ele

    for j in range(len(arr)-1,-1,-1):
        while stack2 and stack2[-1][0]>=arr[j]:
            stack2.pop()
        if not stack2:
            right.append(len(arr))
        else:
            right.append((stack2[-1][1]))
        stack2.append((arr[j],j))
    right=right[::-1]
    print(left,right)

    # difference between left and right smaller elemet index gives you width
    # width * heigth gives you area of histogram

    for i in range(len(arr)):
        cur=arr[i]*(right[i]-left[i]-1)
        histo=max(histo,cur)
    return histo

print(Largest_area_histogram([4,2,1,4,4,1,3]))