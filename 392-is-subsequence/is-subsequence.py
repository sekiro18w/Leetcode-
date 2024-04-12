class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        n=len(s)
        m=len(t)
        cur_len=0
        while i<n and j<m:
            if s[i]==t[j]:
                cur_len+=1
                i+=1
            j+=1
        return cur_len==n
            
            
            
        