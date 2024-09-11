class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        L = list(columnTitle)[::-1]
        s = 0
        for i in range(len(L)): 
            s += (ord(L[i].lower())-96)*26**i
        return s
