class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l_sub = [[]]
        current = l_sub[-1]
        for letter in s:
            if letter in current:
                index = current.index(letter)
                l_sub.append(current[index+1:])
                current = l_sub[-1]
            current.append(letter)
        l_sub = [set(sublist) for sublist in l_sub]
        return len(max(l_sub, key=len))
