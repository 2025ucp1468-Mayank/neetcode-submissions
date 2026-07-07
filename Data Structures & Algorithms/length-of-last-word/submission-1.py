class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i=0
        s=s.strip()
        for j in range(len(s)):
            if s[j]==" ":
                i=j+1
        return len(s)-i 