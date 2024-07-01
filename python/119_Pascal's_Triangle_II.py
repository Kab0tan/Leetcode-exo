class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        else:    
            M = [1,1]
            for i in range(rowIndex-1):
                tmp =[1]
                for j in range(1,len(M)):
                    tmp.append(M[j]+M[j-1])
                tmp.append(1)
                M=tmp
            return M
