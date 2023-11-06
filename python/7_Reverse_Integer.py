class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        a = ""
        if x[0] =='-':
            a = "-"
            x = x[1:]
        if x[-1] == 0:
            return int(a+x[-2::-1]) if -2**31<int(a+x[-2::-1])<2**31-1 else 0
        return int(a+x[::-1]) if -2**31<int(a+x[::-1])<2**31-1 else 0
