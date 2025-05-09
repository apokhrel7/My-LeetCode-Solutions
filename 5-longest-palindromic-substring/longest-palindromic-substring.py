class Solution:
    def longestPalindrome(self, s: str) -> str:

        # can be even or odd
        if len(s) == 1: return s

        max_length = ''
        for i in range(len(s)):
            
            # even
            left, right = i, i
        
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left) + 1 > len(max_length):
                    max_length = s[left:right+1]
                left -= 1
                right += 1  


            #odd
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left) + 1 > len(max_length):
                    max_length = s[left:right+1]
                left -= 1
                right += 1  
        

        return max_length