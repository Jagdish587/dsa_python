
      
# https://leetcode.com/problems/missing-number/
if __name__ == '__main__':

    nums1 = [9,6,4,2,3,5,7,0,1]
    # missing num = 8
    xor_array = 0
    xor2_array = 0
    n = len(nums1)

    # xor all array elements
    for i in range(n):
        xor_array = xor_array ^ nums1[i]

    for i in range(0, n+1):
        xor2_array = xor2_array ^ i
     

    print("xor_array = ", xor_array)
    print("xor2_array2 = ", xor2_array)

    result = xor_array ^ xor2_array
    print("result = ", result)



