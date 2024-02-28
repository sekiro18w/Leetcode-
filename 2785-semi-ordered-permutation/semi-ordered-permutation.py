class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        c=0
        f=0
        l=0
        for i in range(len(nums)):
            if f and l:
                break
            if nums[i]==1:
                f=i
            
            if nums[i]==len(nums):
                l=i
        
        if f<l:
            return f+(len(nums)-l-1)
        else:
            return f+(len(nums)-l-1)-1
                
            