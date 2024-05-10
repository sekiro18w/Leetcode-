class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n=len(arr)
        a=arr

        dic={}

        for i in range(n):
            for j in range(i+1,n):
                if a[i]/a[j] not in dic:
                    dic[a[i]/a[j]]=(a[i],a[j])
        
        return sorted(dic.items(),key=lambda x:x[0])[k-1][1]

        