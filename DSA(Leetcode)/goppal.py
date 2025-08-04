# s = "3[a]2[bc]" ->  aaabcbc

s = "3[a]2[bc]"
n = len(s)
string = ""
i = 0

while i < n:
    if s[i].isdigit():
        ct = int(s[i])  
        i += 1
        if s[i] == '[':
            i += 1
            temp = ""
            while s[i] != ']':
                temp += s[i]
                i += 1
            string += temp * ct  
            i += 1 
    else:
        i += 1  

print(string)
