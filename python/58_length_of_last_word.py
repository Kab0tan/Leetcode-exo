class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s= s[::-1]
        while s[0] == " ":
            s = s[1:]
        if s == " ":
            return 0
        elif len(s) == 1 and s !=" ":
            return 1
        else:
            if " " in s:
                i=0
                while s[i] != " ":
                    i+=1
                return i
            else:
                return len(s)
