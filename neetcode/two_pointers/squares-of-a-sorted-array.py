# https://leetcode.com/problems/squares-of-a-sorted-array/description/
# 977. Squares of a Sorted Array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lhs = 0
        rhs = len(nums) - 1
        end_index = len(nums) - 1
        result = [0] * len(nums)
        print("inital ...", result)
        while lhs <= rhs:
            print("end_index =",end_index)
            lhs_sqr = nums[lhs] ** 2
            rhs_sqr = nums[rhs] ** 2
            result[end_index] = max(lhs_sqr, rhs_sqr)
            print("value ", result[end_index])
            end_index = end_index - 1
            if lhs_sqr >= rhs_sqr:
                lhs = lhs + 1
            else:
                rhs = rhs - 1
        
        return result
