# https://leetcode.com/problems/rotate-array/
# 189. Rotate Array
from collections import deque
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dq = deque(nums)
        dq.rotate(k)
        nums[:] = list(dq)