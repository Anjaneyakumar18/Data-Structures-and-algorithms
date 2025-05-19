class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        out_put = []
        
        def track(dummy, start):
            if sum(dummy) == target:
                out_put.append(list(dummy))
                return
            elif sum(dummy) > target:
                return
            
            for i in range(start, len(candidates)):
                dummy.append(candidates[i])
                track(dummy, i)
                dummy.pop()
        
        track([], 0)
        return out_put
