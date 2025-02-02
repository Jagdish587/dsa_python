# https://neetcode.io/problems/anagram-groups
# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        for str in strs:
            sort_str = ''.join(sorted(str))
            my_dict[sort_str].append(str)
        return list(my_dict.values())


