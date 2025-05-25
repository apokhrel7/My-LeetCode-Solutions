class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: return len(s)

        max_length = 0
        seen_chars = set()  # track characters that you have seen already
        left = 0

        
        for i in range(len(s)):

            # if we see that there are duplicate subsequent characters, move the pointer until there aren't any duplicates
            while s[i] in seen_chars:
                seen_chars.remove(s[left])  # REMEMBER to remove the character first then increment left pointer
                left += 1
            
            seen_chars.add(s[i])

            max_length = max(max_length, i - left + 1)


        return max_length



        