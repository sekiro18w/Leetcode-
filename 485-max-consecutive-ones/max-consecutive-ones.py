class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxLength=0
        curLength=0
        n=len(nums)
        if nums==[0]*n:
            return 0
        if n==1:
            return 1 if nums[0]==1 else 0
        for i in range(n-1):
            if nums[i]==nums[i+1] and nums[i]==1:
                curLength+=1
            else:
                if nums[i]!=1:
                    curLength+=1
                    maxLength=max(maxLength,curLength)
                    curLength=0
        maxLength=max(maxLength,curLength+1)
        return maxLength
            
        