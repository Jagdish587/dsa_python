import heapq


mylist = [5,8,6]

heapq.heapify(mylist)
# print("values = ", mylist)
# print("type = ", type(mylist))

# heapq.heappush(mylist, 7)
# print("values = ", mylist)

# val = heapq.heappop(mylist)
# print("val = ", val)

# print("values = ", mylist)

# push item on list and then pop
# 5, 8, 6
ret = heapq.heappushpop(mylist, 3)
print("ret = ", ret)
print("values = ", mylist)

# pop then return smallest value and then push item
ret = heapq.heapreplace(mylist, 2)
print("ret = ", ret)
print("values = ", mylist)


mylist = [6, 7, 9, 4, 3, 5, 8, 10, 1]
heapq.heapify(mylist)

print("three largest elements = ", heapq.nlargest(2, mylist))
print("three smallest elements = ", heapq.nsmallest(2, mylist))