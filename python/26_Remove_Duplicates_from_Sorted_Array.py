class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = list(set(nums))
        L.sort()
        for i in range(len(L)):
            nums[i] = L[i]
        return len(L)
