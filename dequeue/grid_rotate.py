
# https://leetcode.com/problems/shift-2d-grid/
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        dq = deque(sum(grid, []))
        dq.rotate(k)
        flatten = list(dq)

        result = []

        for i in range(m):
            res = flatten[i*n : (i+1)*n]
            result.append(res)
        return result
        