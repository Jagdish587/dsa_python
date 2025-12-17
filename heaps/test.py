nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
result_list = []
for value_1 in nums1:
  for value_2 in nums2:
    value = (value_1, value_2)
    result_list.append(list(value))
print(result_list)