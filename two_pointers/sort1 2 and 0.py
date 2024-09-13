def sort(nums:list[int])->list[int]:

    zeros=0
    ones=0
    twos=len(nums)-1

    while twos>ones:
        if nums[ones]==0:
            nums[zeros],nums[ones]=nums[ones],nums[zeros]
            zeros+=1

        elif nums[ones]==2:
            nums[twos],nums[ones]=nums[ones],nums[twos]
            twos-=1

        else:
            ones+=1

    return nums

print(sort([1,2,0,1,2,0,0,2,1,2,1,0]))


# brute force 
# brute force
# brute force

def BruteForce(nums:list[int])->list[int]:
    ones=0
    zeros=0
    twos=0
    for num in nums:
        if num==1:
            ones+=1
        elif num==2:
            twos+=1
        else:
            zeros+=1
    

    return [0]*zeros+[1]*ones+[2]*twos

print(BruteForce([1,2,1,2,1,0,0,0,2,1,2,0,1,0,0,2]))