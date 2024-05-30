class Solution:
    def myAtoi(self, s: str) -> int:
        acc = ""
        s = s.strip()
        if not s: 
            return 0
        if s[0] in ['-', '+'] or s[0].isdigit():
            acc+= s[0]
            if len(s) > 1:
                s = s[1:]
                for letter in s:
                    if not letter.isdigit():
                        break
                    acc+= letter
                try:
                    if int(acc) > 2**31-1:
                        return 2**31-1
                    elif int(acc) < -2**31:
                        return -2**31
                    return int(acc)
                except ValueError:
                    return 0
            if s[0].isdigit():
                return int(acc)
            return 0
        return 0
        
