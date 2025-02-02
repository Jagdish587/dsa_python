# https://leetcode.com/problems/find-closest-number-to-zero/
# Two approaches

from collections import defaultdict
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        my_dict = defaultdict(list)
        for num in nums:
            distance = abs(num)
            my_dict[distance].append(num)
        min_key = min(my_dict)
        return max(my_dict[min_key])
        


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest_value = nums[0]

        for num in nums:
            if abs(closest_value) > abs(num):
                closest_value = num
            
        if closest_value < 0 and abs(closest_value) in nums:
            return abs(closest_value)
        else:
            return closest_value