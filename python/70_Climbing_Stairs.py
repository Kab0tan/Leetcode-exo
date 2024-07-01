class Solution:
    def climbStairs(self, n: int) -> int:
        L = [1, 1]+[0]*(n-1)
        for i in range(2,n+1):
            L[i]=L[i-1] + L[i-2]

        return L[n]
