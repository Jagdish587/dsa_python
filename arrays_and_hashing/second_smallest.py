def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    # Write your code here.
    max_element = a[0]
    second_max_element = -1
    smallest_element = a[0]
    

    for i in range(1,n):
        if(a[i] > max_element):
            second_max_element = max_element
            max_element = a[i]
        elif(a[i] > second_max_element):
            second_max_element = a[i]
    
    
    second_smallest = max_element
    for i in range(1,n):
        if(a[i] < smallest_element):
            second_smallest = smallest_element
            smallest_element = a[i]
        elif(a[i]) < second_smallest:
            second_smallest = a[i]


    print("second_max_element = ",second_max_element)
    print("second_smallest = ", second_smallest)

if __name__ == '__main__':
    arr = [3,4,5,2]
    
    getSecondOrderElements(len(arr), arr)

    a = [4,5,4,4,4]
    n = len(a)    
    for i in range(0, n-1):
        if(a[i+1] < a[i]):
            print("not sorted")
    




