
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# 167. Two Sum II - Input Array Is Sorted
# https://neetcode.io/problems/two-integer-sum-ii?list=neetcode150

### using dicntionry , same solition of TWO SUM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        my_dict = {}
        for index, value in enumerate(numbers):
            difference = target - value
            if difference in my_dict:
                return[my_dict[difference]+1, index+1]
            my_dict[value] = index


### using TWO Pointer
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lhs = 0
        rhs = len(numbers) - 1

        while lhs < rhs:
            difference = numbers[rhs] + numbers[lhs]
            if difference == target:
                return[lhs+1, rhs+1]
            if difference > target:
                rhs = rhs -1
            else:
                lhs = lhs + 1

