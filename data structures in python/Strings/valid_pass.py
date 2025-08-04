'''
take an input string from user and check whether the string is valid password?
for it to be valid password, it should satisfy the rules below
    
1. atleast 8 characters in the password
2. atleast one uppercase
3. atleast one lowercase
4. atleast one digit
5. atleast one special symbol
'''
s=input()
if(len(s)<8):
    print("invalid password")
else:
    u=0
    l=0
    d=0
    ss=0
    for i in s:
        if i.isupper():
            u+=1
        elif i.islower():
            l+=1
        elif i.isdigit():
            d+=1
        else:
            ss+=1
    if(u>0 and l>0 and d>0 and ss>0):
        print("valid password")
    else:
        print("not valid")

