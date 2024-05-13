# https://leetcode.com/problems/top-k-frequent-elements/solutions/4910699/beat-96-13-full-explanation/
import heapq
from collections import Counter

def top_k_frequency_elements(nums, k):
    mylist = []
    valueKV = Counter(nums)
    heapq.heapify(mylist)

    for num, frequency in valueKV.items():
        heapq.heappush(mylist, (frequency, num))

    values = heapq.nlargest(k, mylist)
    resultant = [kv[1] for kv in values]
    return resultant

def top_k_frequency_elements_optimized(nums, k):
    mylist = []
    valueKV = Counter(nums)
    mynewlist = valueKV.most_common(k)
    print("valueKV = ", valueKV)
    print("mynewlist = ", mynewlist)
    resultant = [kv[0] for kv in mynewlist]
    print("resultant = ", resultant)

if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    k = 2
    top_k_frequency_elements_optimized(nums, k)
