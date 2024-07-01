class Solution:
    def mySqrt(self, x: int) -> int:
        if x != 0:
            a = x
            for i in range(20):
                a = x/(2*a)+a/2
            return int(a)
        else:
            return 0
