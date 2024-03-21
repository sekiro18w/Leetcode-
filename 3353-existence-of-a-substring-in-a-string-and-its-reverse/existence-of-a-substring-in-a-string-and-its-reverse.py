class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        
        g=s[::-1]
        for i in range(len(s)-2+1):
            if s[i:i+2] in g:
                return True
        
        return False
        