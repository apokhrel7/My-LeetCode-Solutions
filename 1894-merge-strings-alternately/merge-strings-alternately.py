class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = ""


        # loop using length of the longest word
        longest_word = max(len(word1), len(word2))


        for i in range(longest_word):
            if i < len(word1):
                res += word1[i]

            if i < len(word2):
                res += word2[i]

        return res





