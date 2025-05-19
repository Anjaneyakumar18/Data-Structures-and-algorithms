class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        dp=[0]*(n+1)
        dp[1]=1
        dp[2]=2
        i=3
        while i<=n:
            dp[i]=dp[i-1]+dp[i-2]
            i+=1
        return  dp[-1]

        # def rec(current_sum):
        #     if current_sum==n:
        #         nonlocal ways
        #         ways+=1
        #         return
        #     if current_sum > n:
        #         return            
        #     rec(current_sum + 1)
        #     rec(current_sum + 2)

        # ways=0
        # rec(0) 
        # return ways


