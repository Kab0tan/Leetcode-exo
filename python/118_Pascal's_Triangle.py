class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        M = [[1]]
        for i in range(numRows-1):
            L=M[-1]
            tmp = [1]
            for j in range(1,len(L)):
                tmp.append(L[j]+L[j-1])
            tmp.append(1)
            M.append(tmp)
        return M
