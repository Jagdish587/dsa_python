import heapq

if __name__ == '__main__':
    nums1 = [1,7,11]
    nums2 = [2,4,6]
    k = 3
    
    minHeap = []
    ans = []

    heapq.heappush(minHeap, (nums1[0] + nums2[0], 0, 0))

    while minHeap and len(ans) < k:
        sum, i, j = heapq.heappop(minHeap)
        print(sum, i, j)
        ans.append([nums1[i], nums2[j]])
        
        if i + 1 < len(nums1):
            heapq.heappush(minHeap, (nums1[i+1] + nums2[j], i, j+1))

        if j + 1 < len(nums2):
            heapq.heappush(minHeap, (nums1[i] + nums2[j+1], i, j+ 1))
    
    print("ans = ", ans)