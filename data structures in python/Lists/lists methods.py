# l=["hhjvdj","Dsff","dgerg","gerg","reg"]
# print(len(l))
# print(max(l,key=len))
# print(min(l,key=len))


# l=[2,3,5,2,5,8,9,2,2,2]
# print(len(l))
# print(max(l))
# print(min(l))
# print(sum(l))
# print(l.index(5))
# print(l.count(2))

# l="2 3 4 5"
# print(l.split('3'))

# to take string elements from user and split() returns a list of user input
# l=input().split()
# print(l,type(l))

# to convert input().split() into integers(way1)
# l=input().split()
# for i in range(len(l)):
#     l[i]=int(l[i])
# print(l)


# elegant way of using for loop is list comprehension
# l=[2,6,9,0]
# l1=[i*i for i in l if i%2==0]
# print(l1)


# to convert input().split() into integers(way2)
# l=[int(i) for i in input().split()]
# print(l)

# to convert input().split() into integers(way3)
l=list(map(int,input().split()))
print(l)

