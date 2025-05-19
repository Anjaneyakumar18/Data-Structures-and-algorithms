class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        prev = nums[:]
        nums.sort()
        
        def backtrack(permutation):
            if len(permutation) == len(nums):
                result.append(permutation[:])
                return
            for num in nums:
                if num in permutation:
                    continue
                permutation.append(num)
                backtrack(permutation)
                permutation.pop()
        
        result = []
        backtrack([])
        
        for i in range(len(result)):
            if result[i] == prev:
                next_perm = result[(i + 1) % len(result)]
                for j in range(len(nums)):
                    nums[j] = next_perm[j]
                return
