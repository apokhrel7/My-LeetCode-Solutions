class Solution:
    def longestPalindrome(self, s: str) -> int:
        # if odd palindrome, then need even number of letters + 1 odd
        # if even palindrome, then need all even number of letters

        hashMap = {}

        # {a: 1, b:1, c:4, d: 2}
        count = 0


        for char in s:
            if char not in hashMap:
                hashMap[char] = 1
            else:
                hashMap[char] += 1

                if hashMap[char] % 2 == 0:
                    count += 2

        if count < len(s):
            count += 1


        return count

        







        

