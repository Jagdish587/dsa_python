# https://leetcode.com/problems/reverse-string/submissions/1652946859/
# 344. Reverse String
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lhs = 0
        rhs = len(s) - 1

        while lhs <= rhs:
            s[lhs], s[rhs] = s[rhs], s[lhs]
            lhs = lhs + 1
            rhs = rhs - 1
