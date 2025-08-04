s1=int(input())
s2=int(input())
s3=int(input())
s4=int(input())
s5=int(input())
total=s1+s2+s3+s4+s5
percentage=(total/500)*100
if(s1<45 or s2<45 or s3<45 or s4<45 or s5<45):
    print("Fail")
else:
    if(percentage>=75):
        print("Grade A")
    elif(60<=percentage<=74):
        print("Grade B")
    elif(45<=percentage<=59):
        print("Grade C")
    else:
        print("Fail")