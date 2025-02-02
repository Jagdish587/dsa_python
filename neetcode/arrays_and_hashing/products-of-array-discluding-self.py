class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = 1
        result_arr = [1] * len(nums)

        for i in range(len(nums)):
            result_arr[i] = result
            result =  result * nums[i]
        
        result = 1
        for i in range(len(nums)-1, -1, -1):
            result_arr[i] *= result
            result = result * nums[i]
        
        return result_arr
        