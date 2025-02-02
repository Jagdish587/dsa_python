
# https://leetcode.com/problems/divide-array-into-equal-pairs
# 2206. Divide Array Into Equal Pairs

from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        def has_odd_value(d):
            return any(value % 2 != 0 for value in d.values())
        frequency = Counter(nums)
        return not has_odd_value(frequency)
