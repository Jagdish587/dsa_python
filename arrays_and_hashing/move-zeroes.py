class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_pos = 0
        for current_pos, val in enumerate(nums):
            if val:
                # swap elements
                nums[insert_pos], nums[current_pos] = nums[current_pos], nums[insert_pos]
                insert_pos = insert_pos + 1
