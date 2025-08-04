"""
unique word extractor-> take a string from user and print all the unique
words in the string  
 
ip-> python program easy program very easy
op-> python
very
"""

s=input().split()
d={i:0 for i in s}
for i in s:
    d[i]+=1
# for i in d:
#     if d[i]==1:
#         print(i,end=" ")

