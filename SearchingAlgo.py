import bisect

a = [2,1,3,5,6,3]

#Linear search using 'in'
print(6 in a)

#Linear search using 'count'
print(a.count(6))

#Binary search using bisect
pos = bisect.bisect_left(a,6)
print("Index: ",pos)
