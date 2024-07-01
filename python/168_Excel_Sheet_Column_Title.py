class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        L = []
        x = columnNumber
        while x//26 != 0:
            print(x,x%2)
            if x%26 == 0:
                x = x//26-1
                print(x)
                L.append(chr(26+64))
            else:
                L.append(chr(x%26+64))
                x=x//26
        if x != 0:
            L.append(chr(x+64))
        return ''.join(L[::-1])
