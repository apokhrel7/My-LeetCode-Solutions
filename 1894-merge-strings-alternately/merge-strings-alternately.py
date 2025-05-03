class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr = 0
        merged = ''

        while ptr < len(word1) and ptr < len(word2):
            merged += word1[ptr]
            merged += word2[ptr]

            ptr += 1

        if ptr < len(word1):
            merged += word1[ptr:]

        elif ptr < len(word2):
            merged += word2[ptr:]

        return merged

        



        