class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert to max-heap using negatives
        heap_list = [-stone for stone in stones]
        heapq.heapify(heap_list)

        while len(heap_list) > 1:
            largest = -heapq.heappop(heap_list)
            nextlargest = -heapq.heappop(heap_list)

            if largest != nextlargest:
                heapq.heappush(heap_list, -(largest - nextlargest))
        
        if heap_list:
            return -heap_list[0]
        else:
            return 0

        
