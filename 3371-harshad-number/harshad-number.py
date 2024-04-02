class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        
        ans=0
        new=x
        while new:
            ans+=(new%10)
            new//=10
        
        if (x)%ans==0:
            return ans
        return -1