class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)-1
        
        
        while n-1>=0 and nums[n]>=nums[n-1]:
            n-=1
            
        if n==0:
            return True
        
        start=n
        end=n-1
        
        while start!=end:
            if nums[start]>nums[(start+1)%len(nums)]:
                return False
            start=(start+1)%len(nums)
        
        return True