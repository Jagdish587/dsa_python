# https://neetcode.io/problems/longest-consecutive-sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums = set(nums)
        maxlength = 0

        for num in setnums:
            if (num - 1) not in setnums:
                length = 0
                while(num+length) in setnums:
                    length += 1
                maxlength =  max(length, maxlength)
        return maxlength 
        




