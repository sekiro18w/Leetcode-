class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        i=0
        maxi=0
        cur=0
        dic={}
        cur_sum=0
        a=nums


        for j in range(len(a)):
            cur_sum+=a[j]
            if a[j] not in dic:
                dic[a[j]]=0
            dic[a[j]]+=1


            if (j-i+1==k):
                if len(dic)==k:
                    maxi=max(maxi,cur_sum)
                cur_sum-=a[i]
                dic[a[i]]-=1
                if dic[a[i]]==0:
                    del dic[a[i]]
                i+=1
        
        return maxi
        
        