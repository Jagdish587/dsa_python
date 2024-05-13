
def reverse(arr, start_pos, end_pos):
    while(start_pos < end_pos):
        arr[start_pos],arr[end_pos] = arr[end_pos],arr[start_pos]
        start_pos = start_pos + 1
        end_pos = end_pos - 1

def rotate_array(arr, k, n):
    print("array = ", arr)
    print("len of array = ", n)

    reverse(arr, 0, n-1)
    reverse(arr, 0, n-k-1)
    print("array = ", arr)
    reverse(arr, n-k, n-1)

    print("reverse = ", arr)


if __name__ == '__main__':
    arr = [1,2,3,4,5]
    n = len(arr)
    k = 2
    rotate_array(arr, k, n)
"""
'arr '= [1,2,3,4,5]
'k' = 1  rotated array = [2,3,4,5,1]
'k' = 2  rotated array = [3,4,5,1,2]
'k' = 3  rotated array = [4,5,1,2,3] and so on.
"""