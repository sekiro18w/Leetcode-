class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c=0
        if flowerbed==[0]:
            return True
        x=len(flowerbed)
        if flowerbed[:2]==[0,0]:
            flowerbed[0]=1
            c+=1
        for i in range(x-3):
            if (flowerbed[i]==1) and (flowerbed[i+1]==0 and flowerbed[i+2]==0 and flowerbed[i+3]==0):
                flowerbed[i+2]=1
                c+=1
            i+=1
        if flowerbed[-2:]==[0,0]:
            flowerbed[-1]=1
            c+=1
        return c>=n