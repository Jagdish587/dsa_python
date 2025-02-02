# https://leetcode.com/problems/top-k-frequent-words/description/
# 692. Top K Frequent Words

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = Counter(words).most_common()
        sorted_frequency = sorted(frequency, key=lambda x: (-x[1], x[0]))
        sorted_values = [value[0] for value in sorted_frequency]
        return sorted_values[0:k]
