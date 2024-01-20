class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        total_maxi=-1
        for i in range(len(colors)):
            cur_maxi=-1
            for j in range(len(colors)):
                if i!=j and colors[i]!=colors[j]:
                    cur_maxi=max(cur_maxi,abs(j-i))
            
            total_maxi=max(total_maxi,cur_maxi)
        
        return total_maxi
                
                    
        