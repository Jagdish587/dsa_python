
import heapq
from collections import Counter

def nearly_sorted_array(nums, k):
    # into a heapq , add k+1 elements from list
    n = len(nums)
    mylist = nums[:k+1]
    heapq.heapify(mylist)
    resultant = []
    for i in range(k+1, n):
        val = heapq.heappop(mylist)
        resultant.append(val)
        heapq.heappush(mylist, nums[i])

    for i in range(0, len(mylist)):
        val = heapq.heappop(mylist)
        resultant.append(val)

    print("resultant = ", resultant)

    # list(heapq.merge(*arrays))
    mynewlist = list(heapq.merge(nums))
    print("mynewlist = ", mynewlist)



if __name__ == '__main__':
    nums = [6, 5, 3, 2, 8, 10, 9]
    k = 3
    nearly_sorted_array(nums, k)
    arr1 = [1,4,5]
    arr2 = [1,3,4]
    arr3 = [2,6]

    values = list(heapq.merge(arr1, arr2, arr3))
    print("values = ", values)

    mylist = [[1,4,5],[1,3,4],[2,6]]
    values_updated = list(heapq.merge(*mylist))
    print("values updated = ", values_updated)