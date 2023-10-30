class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            reste = target - num
            if reste in dict:
                return [dict[reste], i]
            dict[num] = i
        
