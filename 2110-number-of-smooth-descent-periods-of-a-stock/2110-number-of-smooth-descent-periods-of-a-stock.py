class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans=0
        i=0
        cur=1
        for i in range(len(prices)-1):
            if prices[i]-prices[i+1]==1:
                cur+=1
            else:
                ans+=(cur)*(cur+1)//2
                cur=1
        return ans+(cur*(cur+1))//2
        