temp=float(input("Enter the input temperature value: "))
input_scale=input("Enter the scale C,K or F: ")
output_scale=input("Enter the output scale C,K or F: ")
if input_scale=='C':
    if output_scale=='F':
        print(temp*1.8+32)
    elif output_scale=='K':
        print(temp+273.15)
    else:
        print(temp)
elif input_scale=='F':
    if output_scale=='C':
        print((temp-32)/1.8)
    elif output_scale=='K':
        print((temp+459.67)*(5/9))
    else:
        print(temp)
if input_scale=='K':
    if output_scale=='C':
        print(temp-273.15)
    elif output_scale=='F':
        print(temp*9/5-459.67)
    else:
        print(temp)