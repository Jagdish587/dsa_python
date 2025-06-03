# https://leetcode.com/problems/valid-palindrome/description/
# 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(c for c in s if c.isalnum())
        cleaned = cleaned.lower()
        lhs = 0
        rhs = len(cleaned) - 1
        while lhs <= rhs:
            if cleaned[lhs] != cleaned[rhs]:
                return False
            lhs = lhs + 1
            rhs = rhs - 1
        return True

