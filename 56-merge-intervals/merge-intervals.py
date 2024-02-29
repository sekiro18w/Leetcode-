class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans=[]
        arr=intervals
        arr.sort()
        n=len(arr)
        i=0
        while i+1<n:

            x=arr[i][1]
            y=arr[i][0]

            while i+1<n and arr[i+1][0]<=x:
                x=max(x,arr[i+1][1])
                i+=1
            ans.append([y,x])
            i+=1
        if i!=n:
            ans.append(arr[-1])
        return ans
        