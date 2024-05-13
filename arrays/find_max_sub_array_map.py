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
    arr = [1, 2, 3, 1, 1, 1, 1]
    k = 3
    len = n
    """
    n = len(arr) # size of the array.

    preSumMap = {}
    Sum = 0
    maxLen = 0
    for i in range(n):
        # calculate the prefix sum till index i:
        Sum += arr[i]

        # if the sum = k, update the maxLen:
        if Sum == k:
            maxLen = max(maxLen, i + 1)

        # calculate the sum of remaining part i.e. x-k:
        rem = Sum - k

        # Calculate the length and update maxLen:
        if rem in preSumMap:
            length = i - preSumMap[rem]
            maxLen = max(maxLen, length)

        # Finally, update the map checking the conditions:
        if Sum not in preSumMap:
            preSumMap[Sum] = i

    print("maxLen = ", maxLen)
        

# Driver Code
arr = [-1,-1,1]
k = 0
n = len(arr)

max_len_sub_array(arr, n, k)