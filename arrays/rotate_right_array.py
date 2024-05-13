
def reverse(arr, start_pos, end_pos):
    while(start_pos < end_pos):
        arr[start_pos],arr[end_pos] = arr[end_pos],arr[start_pos]
        start_pos = start_pos + 1
        end_pos = end_pos - 1

def rotate_array(arr, k, n):
    print("array = ", arr)
    print("len of array = ", n)

    reverse(arr, 0, n-1)
    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)

    print("reverse = ", arr)


if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7]
    n = len(arr)
    k = 3
    rotate_array(arr, k, n)
"""
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
7->6->5->4->3->2-1
5->6->7->4->3->2->1
"""