class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans=[0]*len(arr)
        maxi=-1
        for i in range(len(arr)-1,-1,-1):
            ans[i]=maxi
            maxi=max(arr[i],maxi)
        return ans
        