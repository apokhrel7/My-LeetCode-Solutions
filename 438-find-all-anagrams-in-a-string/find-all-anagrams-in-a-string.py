class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        ### SLIDING WINDOW ###
        # Time-complexity: O(len(s))
        # Space-complexity: O(26) --> 26 lowercase English letters

        if len(p) > len(s): return []
        
        # keep count of the first len(p) characters in s
        count_s = {}
        for i in range(len(p)):
            if s[i] not in count_s:
                count_s[s[i]] = 1
            else:
                count_s[s[i]] += 1

        # keep count of characters in p 
        count_p = {}
        for char in p:
            if char not in count_p:
                count_p[char] = 1
            else:
                count_p[char] += 1

        res = []
        if count_p == count_s:
            res = [0]
        else:
            res = []

        left_ptr = 0
        for r_ptr in range(len(p), len(s)):
            if s[r_ptr] not in count_s:
                count_s[s[r_ptr]] = 1
            else:
                count_s[s[r_ptr]] += 1

            count_s[s[left_ptr]] -= 1

            if count_s[s[left_ptr]] == 0:
                count_s.pop(s[left_ptr])

            left_ptr += 1
            if count_s == count_p:
                res.append(left_ptr)
            

        return res