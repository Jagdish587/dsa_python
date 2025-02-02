# https://leetcode.com/problems/first-unique-character-in-a-string/description/
# 387. First Unique Character in a String

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        position = -1
        unique_character = 1
        frequency = Counter(s)
        if unique_character in frequency.values():
            for key,value in frequency.items():
                if unique_character == value:
                    first_unique_char = key
                    position = s.index(first_unique_char)
                    break
        return position


