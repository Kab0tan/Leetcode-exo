class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = [str(i) for i in digits]
        b = ''.join(a)
        c = int(b)+1
        return [int(i) for i in str(c)]
