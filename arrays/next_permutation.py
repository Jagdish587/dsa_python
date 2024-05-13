arr = [1,4,5,8,7]


def next_permutation(arr, n):
    
    """
    step 1: find pivot element
    """
    n = len(arr)
    for i in range(n-1,0,-1):
        #print(arr[i], end = " ")
        if(arr[i] > arr[i-1]):
            pivot = i -1
            break
    else:
        arr.reverse()
        return
    
    swap_index = n -1 
    while(swap_index >= pivot):
        if(arr[swap_index] > arr[pivot]):
            arr[swap_index], arr[pivot] = arr[pivot], arr[swap_index]
            break
        swap_index = swap_index -1

    arr[pivot+1:] = reversed(arr[pivot+1:])
    return

# 1,2,3
# 3,2,1
# 

if __name__ == '__main__':
    arr = [1,4,5,8,7]
    n = len(arr)
    print("arr = ", next_permutation(arr, n))
