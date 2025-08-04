s = "foo"
t = "bar"
d={}
if(len(s)!=len(t)):
    print("not isomorphic")
else:
    for i in range(len(s)):
        if s[i] in d:
            if d[s[i]]==t[i]:
                continue
            else:
                
                print("not isomorphic")
                break
        else:
            d[s[i]]=t[i]
    else:
        print("isomorphic")