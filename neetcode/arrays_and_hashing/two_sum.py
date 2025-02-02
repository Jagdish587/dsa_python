class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for index, value in enumerate(nums):
            diff = target -  value
            if diff in my_dict:
                return [my_dict[diff], index]
            my_dict[value] = index
        
