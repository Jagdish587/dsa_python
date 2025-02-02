# https://neetcode.io/problems/longest-consecutive-sequence
# https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0
        set_nums = set(nums)
        max_length_sequence = 0

        for num in set_nums:
            if (num -1) not in set_nums:
                # find element which does not have left neighbour
                # i.e first element
                length = 0
                while(num+length) in set_nums:
                    length = length + 1
                max_length_sequence = max(length, max_length_sequence)
        return max_length_sequence
        




