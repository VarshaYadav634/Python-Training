# # union
# a={2,5,9,6}
# b={2,5,7,8}
# print(a.union(b),a,b)
# print(a|b,a,b)
# print(a.update(b),a,b)


# # intersection
# a={2,5,9,6}
# b={2,5,7,8}
# print(a.intersection(b),a,b)
# print(a&b,a,b)
# print(a.intersection_update(b),a,b)


# # difference
# a={2,5,9,6}
# b={2,5,7,8}
# print(a.difference(b),a,b)
# print(a-b,a,b)
# print(a.difference_update(b),a,b)


# # symmetric difference
# a={2,5,9,6}
# b={2,5,7,8}
# print(a.symmetric_difference(b),a,b)
# print(a^b,a,b)
# print(a.symmetric_difference_update(b),a,b)

# # superset,subset,disjointset,len,min,max,sum
a={2,5,9,6}
b={2,5,7,8}
print(a.issuperset(b))
print(a.issubset(b))
print(a>b)
print(b>a)
print(a.isdisjoint(b))
print(len(a))
print(max(a))
print(sorted(a))