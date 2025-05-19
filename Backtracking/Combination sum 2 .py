from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        
        def dfs(comb, start, target):
            if target == 0:
                result.append(comb.copy())
                return
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                comb.append(candidates[i])
                dfs(comb, i + 1, target - candidates[i])
                comb.pop()
        
        dfs([], 0, target)
        return result
