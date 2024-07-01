import copy 

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1  or s[0] in "})]":
            return False
        else:
            map = {
                "(":")",
                "[":"]",
                "{":"}"
            }
            m = []
            for i in s:
                if i in "{([" :
                    m.append(i)
                elif len(m)!=0 and i == map[m[-1]]:
                    m.pop()
                else:
                    return False
            return m == []
