class Solution:
    def romanToInt(self, s: str) -> int:
        tot = 0
        i=0
        if len(s) == 1:
            next_letter = 0
        while i != len(s):
            if  i <len(s)-1:
                next_letter = s[i+1]
            current = s[i]
            if current == "M":
                tot+= 1000
            elif current =="D":
                tot+= 500
            elif current =="C":
                if next_letter == "D":
                    tot+=400
                    i+=1
                elif next_letter == "M":
                    tot+=900
                    i+=1
                else:
                    tot+= 100
            elif current =="L":
                tot+= 50
            elif current =="X":
                if next_letter == "L":
                    tot+=40
                    i+=1
                elif next_letter == "C":
                    tot+=90
                    i+=1
                else:
                    tot+= 10
            elif current =="V":
                tot+= 5
            elif current =="I":
                if next_letter == "V":
                    tot+=4
                    i+=1
                elif next_letter == "X":
                    tot += 9
                    i+=1
                else:
                    tot+= 1
            i+=1

        return tot
