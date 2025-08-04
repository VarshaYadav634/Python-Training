'''
you have to take an input string and print frequency of each word
 
ip-> python program easy program very easy
op-> python : 1
program : 2
easy: 2
very : 1
'''
s=input().split()
d={i:0 for i in s}
for i in s:
    d[i]+=1
print(d)
