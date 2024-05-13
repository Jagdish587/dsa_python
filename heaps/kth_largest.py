import heapq


def find_kth_largest(nums, k):
    heapq.heapify(nums)
    val = heapq.nlargest(k, nums)
    print("val = ", val)
    return val[k-1]


if __name__ == '__main__':
    nums = [3,2,1,5,6,4]
    k = 2
    value = find_kth_largest(nums, k)
    print("value = ", value)