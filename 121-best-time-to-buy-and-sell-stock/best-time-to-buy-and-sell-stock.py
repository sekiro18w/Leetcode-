class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        buy_price=prices[0]
        
        for i in range(1,len(prices)):
            
            if buy_price>prices[i]:
                buy_price=prices[i]
            else:
                cur=prices[i]-buy_price
                ans=max(ans,cur)
        
        return ans
            
            
        
        
            
        