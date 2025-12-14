## https://leetcode.com/problems/k-closest-points-to-origin/description/
## 973. K Closest Points to Origin
import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heaplist = []
        for value in points:
            distance = math.sqrt((value[0])**2 + (value[1])**2)
            heapq.heappush(heaplist, (distance, value))

        output = heapq.nsmallest(k, heaplist)
        return [value for _, value in output]
        