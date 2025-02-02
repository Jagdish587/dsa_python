

# https://leetcode.com/problems/sort-characters-by-frequency/
# 451. Sort Characters By Frequency

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        result_str = ""
        frequency = Counter(s).most_common()
        for value in frequency:
            result_str = result_str+value[0]*value[1]
        return result_str

