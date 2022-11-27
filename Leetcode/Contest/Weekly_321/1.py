class Solution:
    def pivotInteger(self, n: int) -> int:
        
        dp = [  0 for _ in range(n+1)]
        
        for i in range(1, n+1):
            dp[i] = (i*(i+1))//2
        
        pivot  = -1 
        # print(dp)
        for i in range(1, n+1):
            if dp[i] == dp[n] - dp[i-1]:
                return i
        
        return -1 