class Solution:
    def scoreOfString(self, s: str) -> int:
        st,sm=len(s),0
        for i in range(1,st):
            sm+=abs(ord(s[i])-ord(s[i-1]))
        return sm