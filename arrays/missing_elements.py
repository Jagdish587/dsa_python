### 268. Missing Number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # step1 : compute xor of all array elements
        xor_arr = 0
        for val in nums:
            xor_arr = xor_arr ^ val

        # step2 : compute xor of all numbers from 0 to n
        xor_nums = 0
        for val in range(0, len(nums)+1):
            xor_nums = xor_nums ^ val

        result = xor_arr ^ xor_nums
        return result
