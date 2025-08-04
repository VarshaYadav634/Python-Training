# time complexity nlogn
class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        s.sort(key=lambda x:int(x[-1]))
        t=""
        for i in s:
            for j in i:
                if j.isalpha():
                    t=t+j
            t=t+" "
        return t.strip()
s=Solution()
print(s.sortSentence("is2 this1 a3 sentence4"))