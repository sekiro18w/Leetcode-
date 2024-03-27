class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        l=0
        r=len(nums)-1
        nums.sort()
        ans=0
        while l<=r:
            
            cur=nums[l]+nums[r]
            if cur<=target:
                ans=(ans+(1<<(r-l)))%(1000000000+7)
                l+=1
            else:
                r-=1
        return ans%(1000000000+7)
                