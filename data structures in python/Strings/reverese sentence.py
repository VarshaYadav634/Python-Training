'''
take a sentence from user and print the sentence in reverse word by word
 
ip-> python programming is easy
op-> easy is programming python
 
'''

# s=input().split()
# print(*s[::-1])         //unpacking


s=input().split()
s=s[::-1]
print(" ".join(s))