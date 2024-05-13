def lenOfLongSubarr(A, N, K):
    sum_index_map = {0: -1}  # Dictionary to store cumulative sum and its index
    maxLen = 0
    prefix_sum = 0

    for i in range(N):
        prefix_sum += A[i]
        
        # If prefix_sum-K is found in the map, update maxLen
        if prefix_sum - K in sum_index_map:
            length = i - sum_index_map[prefix_sum - K]
            maxLen = max(maxLen, length)

        # Store the index of the cumulative sum if it's not already in the map
        if prefix_sum not in sum_index_map:
            sum_index_map[prefix_sum] = i

    return maxLen



def max_len_sub_array(arr, n, k):
    """
    Problem is find max length of sub array
    arr = [10, 5, 2, 7, 1, 9]
    k = 15
    len = n
    """

    # travserse first pointer from index 0 to n-2
    # traverse second pointer from index 1 to n-1
    # if prefix_sum is k , note down delta of distance
    # if prefix sum > k , break inner loop
    max_length = 0
    prefix_sum = 0
    for i in range(0, n):
        prefix_sum = 0
        for j in range(i, n):
            prefix_sum = prefix_sum + arr[j]
            if(prefix_sum == k):
                distance = (j-i +1)
                max_length = max(max_length, distance)
            if(prefix_sum > k):
                break   
    print("max length = ", max_length)
# Driver Code
arr = [1,2,1,2,1]
n = len(arr)
k = 3

for i in range(0, n):
    print("value = ", arr[i])

# # print("Length = " + str(lenOfLongSubarr(arr, n, k)))
max_len_sub_array(arr, n, k)