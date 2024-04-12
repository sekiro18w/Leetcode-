class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if flowerbed==[0]:
            return True
        c=0
        x=len(flowerbed)
        if flowerbed[:2]==[0,0]:
            flowerbed[0]=1
            c+=1
        i=0
        while i<x:
            if flowerbed[i]==1 and flowerbed[i+1:i+4]==[0,0,0]:
                flowerbed[i+2]=1
                c+=1
            i+=1
        if flowerbed[-2:]==[0,0]:
            flowerbed[-1]=1
            c+=1
        return c>=n