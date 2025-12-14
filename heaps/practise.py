import heapq
from collections import Counter

nums = [5, 4, 3, 5, 4, 3, 5, 5, 4]

counter = Counter(nums)
print(counter)
heap = []

# Push (frequency, value) pairs
for num, freq in counter.items():
    heapq.heappush(heap, (freq, num))

print(heap)


# Pop in increasing frequency order
while heap:
    freq, num = heapq.heappop(heap)
    print(num, "appears", freq, "times")
