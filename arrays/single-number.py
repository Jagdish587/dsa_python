### 136. Single Number
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_nums = 0
        for val in nums:
            xor_nums = xor_nums ^ val
        return xor_nums
        
