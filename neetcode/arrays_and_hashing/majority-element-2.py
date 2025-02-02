# https://leetcode.com/problems/majority-element-ii/

from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        frequency = Counter(nums)
        check = len(nums)/3
        return [key for key,values in frequency.items() if values > check]
        
