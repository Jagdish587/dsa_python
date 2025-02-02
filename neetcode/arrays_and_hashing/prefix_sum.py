from collections import defaultdict

def subarraySum(nums, k):
    prefix_sum_count = defaultdict(int)
    prefix_sum_count[0] = 1  # Base case: Prefix sum 0 occurs once

    prefix_sum = 0
    count = 0

    for num in nums:
        prefix_sum += num  # Update prefix sum
        count += prefix_sum_count[prefix_sum - k]
        # Update hashmap with current prefix sum
        prefix_sum_count[prefix_sum] = 1 + prefix_sum_count[prefix_sum] 

    return count

# Example usage
nums = [3, 4, 7, 2, -3, 1, 4, 2, 1]
k = 7
result = subarraySum(nums, k)
print("Count of subarrays summing to", k, ":", result)