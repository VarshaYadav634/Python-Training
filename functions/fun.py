# regular arguments
# def fun(a,b):
#     return a+b
# print(fun(3,4))


# def fun(a,b):
#     return a+b
# print(fun('a','b'))

# def fun(a:int,b:int)->int:
#     return a+b
# print(fun('a','b'))

# default arguments
# def fun(a,b=0):
#     return a+b
# print(fun(3))


# def fun(a,b=0):
#     return a+b
# print(fun(3,5))

# keyword argument
# def fun(a,b):
#     print(a,b)
# fun(b=3,a=4)

# variable no. of arguments
# def fun(a,*b):
#     print(a,b)
# fun(3,4,5,6,7,8,9)


# def fun(*a,b):
#     print(a,b)
# fun(3,4,5,6,7,8)  #error because all values are taking by a only


# def fun(*a,b):
#     print(a,b)
# fun(3,4,5,6,7,8,b=9)

# lamda function
# c=lambda a,b:a+b
# print(c(4,5))

# l=[[2,3],[4,5,6],[6,7],[0,9]]
# l.sort(key=lambda x:x[-1]*x[-2])
# print(l)


#Build Calclulator using functions
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def product(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
def floor_Div(a,b):
    print(a//b)
def rem(a,b):
    print(a%b)
def exp(a,b):
    print(a**b)
a,b=map(int,input().split())
print("Select the operation you want to perform: ")
print("1. Addition\n2. Subtraction\n3. Division\n4. Floor Division\n5. Product\n6. Remainder\n7. Power")
n=int(input())
if(n==1):
    add(a,b)
elif(n==2):
    sub(a,b)
elif n==3:
    div(a,b)
elif n==4:
    floor_Div(a,b)
elif n==5:
    product(a,b)
elif n==6:
    rem(a,b)
elif n==7:
    exp(a,b)
else:
    print("Invalid")
