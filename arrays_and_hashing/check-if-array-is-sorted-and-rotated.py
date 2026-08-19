### https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
class Solution:
    def check(self, nums: List[int]) -> bool:

        temp_nums = sorted(nums)
        mydeque = deque(nums)
        k = 1

        for _ in range(len(nums)):
            if temp_nums == list(mydeque):
                return True
            mydeque.rotate(1)
        return False
