class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest_palindrome = ""
        for i in range(len(s)):

            # check for odd palindrome lengths
            l, r = i, i

            # expand left and right pointers, make sure they're in bound, and that a palindrome exists 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                potential_palindrome = s[l : r + 1]

                if len(potential_palindrome) > len(longest_palindrome):
                    longest_palindrome = potential_palindrome

                # starts from i and expands outwards on both sides
                l -= 1
                r += 1

            # check for even palindrome lengths
            l, r = i, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                potential_palindrome = s[l : r + 1]

                if len(potential_palindrome) > len(longest_palindrome):
                    longest_palindrome = potential_palindrome

                l -= 1
                r += 1

        return longest_palindrome
