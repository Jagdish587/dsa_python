## https://leetcode.com/problems/relative-ranks/description/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        result = [0] * len(score)
        heap_list = []

        for index, value in enumerate(score):
            heapq.heappush(heap_list, (-value, index))
            # print(heap_list)

        rank = 1

        while heap_list:
            _, index = heapq.heappop(heap_list)
            if rank == 1:
                result[index] = "Gold Medal"
            elif rank == 2:
                result[index] = "Silver Medal"
            elif rank == 3:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(rank)
            rank = rank + 1
        return result
        
