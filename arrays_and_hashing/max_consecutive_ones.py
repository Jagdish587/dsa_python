
if __name__ == '__main__':

    arr = [1,1,0,1,1,1,0]
    count =  0
    max_count = 0
    # max count here is 3
    n = len(arr)
    for i in range(n):
        if(arr[i] != 0):
            count = count + 1
        else:
            count = 0
        max_count = max(count, max_count)
    
    print("max count = ", max_count)


