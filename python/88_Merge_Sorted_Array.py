class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n==1:
            nums1[-1] = nums2[0]
            nums1.sort()
        elif n>1:
            nums1[-1:-n-1:-1] = nums2
            nums1.sort()
        
