class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        L = {}
        for num in nums:
            if num not in L:
                L[num] = 1
            else:
                L[num]+=1
        for item in L:
            if L[item] == 1:
                return item
