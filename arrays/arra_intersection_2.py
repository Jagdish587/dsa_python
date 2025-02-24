# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
# 350. Intersection of Two Arrays II

from collections import Counter

def intersect(nums1, nums2):
    # Count frequencies
    c1 = Counter(nums1)
    c2 = Counter(nums2)

    result = []

    # Find common elements with min count
    for num in c1:
        if num in c2:
            times = min(c1[num], c2[num])
            result.extend([num] * times)

    return result

