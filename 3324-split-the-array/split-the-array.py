class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        
        dic={}
        
        for i in nums:
            if i not in dic:
                dic[i]=0
            dic[i]+=1
        for i in dic:
            if dic[i]>2:
                return False
        return True