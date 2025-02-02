# sort-array-by-increasing-frequency
# 1636. Sort Array by Increasing Frequency

from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency = Counter(nums)
        def mysortfunc(num):
            return (frequency[num], -num)
        nums.sort(key=mysortfunc)
        return nums

