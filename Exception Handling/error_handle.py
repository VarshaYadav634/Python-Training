# try:
#     l=[1,2,3,4]
#     print(l[4])
# except:
#     print("error occured")
# print("hello world")


try:
    l=[1,2,3,4]
    print(l[4])
except ZeroDivisionError:
    print("zero division")
except IndexError:
    print("index error occured")
print("hello world")