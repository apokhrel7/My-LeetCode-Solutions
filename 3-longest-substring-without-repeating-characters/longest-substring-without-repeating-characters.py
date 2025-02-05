class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        p1 = 0
        seen = set()
        count_length = 0
        max_length = 0

        for i in range(len(s)):

            while s[i] in seen:
                seen.remove(s[p1])
                p1 += 1
                count_length -= 1

            seen.add(s[i])
            count_length += 1

            if count_length > max_length:
                max_length = count_length

        return max_length




            




            



            