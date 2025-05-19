class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def track(start,subset):
            if subset not in result:
                result.append(subset.copy())
            for i in range(start,len(nums)):
                subset.append(nums[i])
                track(i+1,subset)
                subset.pop()
        result=[]
        track(0,[])
        return (result)
