
def intersection(first_arr, second_arr):
        first_array = set(first_arr)
        second_arr = set(second_arr)

        resultant_array = first_array.intersection(second_arr)
        return resultant_array


def union(first_arr, second_arr):
      resultant_arr = list(set(first_arr + second_arr))
      resultant_arr.sort()
      return resultant_arr
      
if __name__ == '__main__':
    nums1 = [1,2,2]
    nums2 = [2,2]

    resultant_array = union(nums1, nums2)
    print("union = ", resultant_array)


    resultant_array = intersection(nums1, nums2)
    print("intersection = ", resultant_array)



