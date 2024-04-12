class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        n=len(s)
        m=len(t)
        cur=''
        while i<n and j<m:
            if s[i]==t[j]:
                cur+=s[i]
                i+=1
            j+=1
        return cur==s
            
            
            
        