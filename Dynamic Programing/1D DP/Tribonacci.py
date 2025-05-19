class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        trib=[0,1,1]
        while len(trib)<=n:
            trib.append(trib[-1]+trib[-2]+trib[-3])
        return trib[-1]
        
