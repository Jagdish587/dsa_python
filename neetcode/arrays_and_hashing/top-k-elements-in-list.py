# https://neetcode.io/problems/top-k-elements-in-list

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        values = Counter(nums).most_common(k)
        return [value[0] for value in values]
