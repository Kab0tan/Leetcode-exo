class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        d = {}
        for i in range(1,numRows+1):
            if i not in d:
                d[i] = '' 
        row = 1
        step = 1
        for letter in s:
            d[row]+= letter
            if row == numRows:
                step= -1
            elif row == 1:
                step= 1
            row += step
        return ''.join(list(d.values()))
