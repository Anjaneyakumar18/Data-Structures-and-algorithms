class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(nums):
            second=nums[0]
            first=max(nums[0],nums[1])
            for i in range(2,len(nums)):
                temp=max(first,second+nums[i])
                second=first
                first=temp
            return max(second,first)

        if len(nums)<4:
            return max(nums)
        return max(helper(nums[:-1]),helper(nums[1:]))
