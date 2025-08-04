a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("Enter a number- \n1. addition\n2. subtraction\n3. multiplication\n4. division")
print("5. floor division\n6. power\n7. remainder")    
c=input()
if(c=='1'):
    print("Addition is",a+b)
elif(c=='2'):
    print("Subtraction is",a-b)
elif c=='3':
    print("Multiplication is",a*b)
elif c=='4':
    print("Division is",a/b)
elif c=='5':
    print("Floor division is",a//b)
elif c=='6':
    print("Power is",a**b)
elif c=='7':
    print("remainder is",a%b)
else:
    print("Invalid! Enter from the given number")