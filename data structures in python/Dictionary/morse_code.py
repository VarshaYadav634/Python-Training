l=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
s="abcdefghijklmnopqrstuvwxyz"
d=dict(zip(s,l))
words=input().split()
st=set()
for i in words:
    x=""
    for ch in i:
        x=x+d[ch]
    st.add(x)
print(st)
print(len(st))