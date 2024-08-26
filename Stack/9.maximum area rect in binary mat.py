## leetcode - hard maximum area rectriangle in a binary matrix
"""

   0  1  1  0
   1  1  1  1
   1  1  1  1
   1  1  0  0


"""

def histogram_area(arr:list[int])->int:
    area=0
    stack=[]
    left=[]
    right=[]


    for i in range(len(arr)):
        if stack and stack[-1][0]>=arr[i]:
            stack.pop()
        if not stack:
            left.append(-1)
        else:
            left.append(stack[-1][1])
        stack.append((arr[i],i))


    stack=[]


    for i in range(len(arr)-1,-1,-1):
        while stack and stack[-1][0]>=arr[i]:
            stack.pop()
        if not stack:
            right.append(len(arr))
        else:
            right.append(stack[-1][1])
        stack.append((arr[i],i))
    right=right[::-1]


    for i in range(len(arr)):
        area = max(area , arr[i]*(right[i]-left[i]-1))


    return area



if __name__=="__main__":
    matrix=[
        [0, 1, 1, 0, 1],
        [1, 1, 0, 1, 1],
        [1, 1, 0, 1, 1],
        [1, 1, 0, 1, 1]
    ]
    final=0

    buildings=[0]*len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                buildings[j]=0
            else:
                buildings[j]+=1
        area=histogram_area(buildings)
        final=max(final,area)
    print(final)