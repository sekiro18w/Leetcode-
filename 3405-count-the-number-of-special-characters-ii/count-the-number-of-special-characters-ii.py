class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans=0
        dic={}
        for i in range(len(word)):
            if word[i] not in dic:
                dic[word[i]]=i
            else:
                if word[i].islower():
                    dic[word[i]]=i
        for i in dic:
            if (i.islower() and i.upper() in dic and dic[i.upper()])>dic[i]:
                ans+=1
        return ans
        
        