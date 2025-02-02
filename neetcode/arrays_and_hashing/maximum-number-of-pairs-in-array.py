# https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/
# 2341. Maximum Number of Pairs in Array

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        no_of_pairs = 0
        left_over = 0
        frequency = Counter(nums)
        sum_pairs = 0
        left_pairs = 0

        for num in frequency.values():
            (pairs, left_over) = divmod(num, 2) 
            sum_pairs += pairs
            left_pairs += left_over
        return [sum_pairs, left_pairs]
        
