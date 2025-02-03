class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s
        
        max_length = 0
        max_length_substring = ''

        def getPalindrome(left, right, substring) -> str:
            while left >= 0 and right <= (len(s) - 1) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left + 1: right]

        for i in range(len(s)):
            #### odd string (start from middle and expand out)
            # left, right = i, i

            # while left >= 0 and right <= (len(s) - 1) and s[left] == s[right]:

            #     if (right - left + 1) > max_length:
            #         max_length = right - left + 1
            #         max_length_substring = s[left:right+1]

            #     left -= 1
            #     right += 1

            #### even string (start with character that is next to the current pointer)
            # left, right = i, i + 1
            # while left >= 0 and right <= (len(s) - 1) and s[left] == s[right]:

            #     if (right - left + 1) > max_length:
            #         max_length = right - left + 1
            #         max_length_substring = s[left:right+1]

            #     left -= 1
            #     right += 1


            # odd
            odd_s = getPalindrome(i, i, s)

            # even
            even_s = getPalindrome(i, i + 1, s)

            if len(odd_s) > len(even_s) and len(odd_s) > max_length:
                max_length = len(odd_s)
                max_length_substring = odd_s

            elif len(even_s) > len(odd_s) and len(even_s) > max_length:
                max_length = len(even_s)
                max_length_substring = even_s

        return max_length_substring









        return max_length_substring

            

            

            





