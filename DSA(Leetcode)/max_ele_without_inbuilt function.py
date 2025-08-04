#find maximum element in an array but without using inbuilt function max or sort.

# using Linear search
# l=[10,96,35,112,45]
# max=l[0]
# maxi=0
# for i in range(len(l)):
#     if l[i]>max:
#         max=l[i]
#         maxi=i
# print(max,maxi)


#find second maximum element in an array but without using inbuilt
# function max or sort.
 
l=[45,36,98,52,10]
max=l[0]
s_max=-9999
for i in range(len(l)):
    if l[i]>max:
        s_max=max
        max=l[i]
    elif l[i]>s_max and l[i]<max:
        s_max=l[i]
print(s_max)

