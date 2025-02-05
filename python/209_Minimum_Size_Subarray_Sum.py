class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        S = 0
        global_min=float('inf')
        for right in range(len(nums)):  
            S+=nums[right] 
            while S >= target: 
                global_min = min(global_min, right-left+1)
                S-= nums[left] 
                left+=1
        if global_min != float('inf'):
            return global_min
        return 0
