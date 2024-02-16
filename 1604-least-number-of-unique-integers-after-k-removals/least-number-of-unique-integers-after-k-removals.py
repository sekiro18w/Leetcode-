class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        dic={}
        
        for i in arr:
            if i not in dic:
                dic[i]=0
            dic[i]+=1
        
        ans=0
        dic=sorted(dic.items(),key=lambda x:x[1])
        for i in dic:
            
            if k>=i[1]:
                k-=i[1]
                ans+=1
            if k<i[1]:
                break
            
          
        return len(dic)-ans
            