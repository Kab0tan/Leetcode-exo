class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        L = {}
        for i in nums:
            if i not in L:
                L[i] = 1
            else:
                L[i]+=1
        return max(L,key=L.get)
