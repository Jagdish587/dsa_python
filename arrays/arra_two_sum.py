# leet code accepted
# 1. Two Sum
# https://leetcode.com/problems/two-sum/submissions/1244339613/

# Also 167. Two Sum II - Input Array Is Sorted

def return_array_indexes(nums, n , target):
    # loop through last but one element
    # and inner loop from 1st element to last element
    for i in range(0, n-1):
        for j in range(i+1, n):
            if(nums[i] + nums[j] == target):
                return [i,j]


def return_indexes(nums, n, target):
    i = 0
    j = n-1
    while(i < j):
        if(nums[i] + nums[j] == target):
            return [i+1,j+1]
        elif(nums[i] + nums[j] > target):
            j = j-1
        else:
            i = i+1


if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    n = len(nums)

    print("values = ", return_array_indexes(nums, n , target))

    numbers = [2,7,11,15]
    target = 9
    n = len(numbers)
    print("values = ", return_indexes(nums, n, target))

    myhashmap = {}
    print("type = ", type(myhashmap))
    

