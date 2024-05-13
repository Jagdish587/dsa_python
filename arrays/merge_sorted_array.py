def sortedArray(a, b):
    # Write your code here
    resultant_array = []

    m = len(a)-1
    n = len(b)-1
    m_index = 0
    n_index = 0

    while(m_index < m or n_index < n):
        if(a[m_index] <= b[n_index]):
                if(a[m_index] not in resultant_array):
                    resultant_array.append(a[m_index])
                m_index = m_index + 1
        elif(b[n_index] < a[m_index]):
            if(b[n_index] not in resultant_array):
                resultant_array.append(b[n_index])
            n_index = n_index + 1
    
    print("m_index = ", m_index)
    print("n_index = ", n_index)
    print("resultant_array = ", resultant_array)

    if(m < n):
        while(m_index <= m):
                if(a[m_index] not in resultant_array):
                    resultant_array.append(a[m_index])
                m_index = m_index + 1
    else:
        while(n_index <= n):
            if(b[n_index] not in resultant_array):
                resultant_array.append(b[n_index])
            n_index = n_index + 1
        
    print("resultant_array = ", resultant_array)
    
    # return resultant_array



if __name__ == '__main__':
     
    a = [1, 2, 2, 2, 3]
    b =  [2, 3, 3, 4, 5, 5]
    arr = list(set(a+b))
    arr.sort()
    print("result = ", arr)

    array_first = set(a)
    array_second =  set(b)

    resultant_array = list(array_first.intersection(array_second))
    print("resultant_array = ", resultant_array)