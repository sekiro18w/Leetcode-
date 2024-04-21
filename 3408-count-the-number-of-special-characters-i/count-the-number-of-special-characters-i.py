class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans=0
        dic={}
        for i in word:
            if i not in dic:
                dic[i]=0
            dic[i]+=1
        for i in dic:
            if (i.islower() and i.upper() in dic):
                ans+=1
        return ans
        