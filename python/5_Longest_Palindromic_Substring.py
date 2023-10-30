#check every substring center. While substring is palindrome, extend substring in L and R, and only keep the substring with longest length.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = '#'+"#".join(s)+'#'
        max_len = 0
        max_sub = ""
        for i in range(1,len(s)-1):
            l = i-1
            r = i+1
            if s[i] == '#':
                sub = ""
                _len = 0
            else:
                sub = s[i]
                _len= 1
            while l>=0 and r<len(s)-1 and s[l] == s[r]:
                if s[l] != '#':
                    _len += 2
                    sub = s[l]+sub+s[r]
                l-=1
                r+=1
            if _len > max_len:
                max_len = _len
                max_sub = sub
        return max_sub

  #--------alternative--------
class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, length = 0, 1
        for i in range(1, len(s)):
            l = i - length
            r = i+1
            s_odd= s[l-1:r] 
            s_even = s[l:r]
            if l - 1 >= 0 and s_odd == s_odd[::-1]:
                start = l - 1
                length += 2
            elif s_even == s_even[::-1]:
                start = l
                length += 1
        return s[start:start+length]
