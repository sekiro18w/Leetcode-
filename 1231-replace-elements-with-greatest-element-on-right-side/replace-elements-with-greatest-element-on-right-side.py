class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans=[]
        ans.append(-1)
        if len(arr)==1:
            return ans
        maxi=-1
        for i in range(len(arr)-1,-1,-1):
            if maxi<arr[i]:
                maxi=arr[i]
            ans.append(maxi)
        ans.pop()
        return ans[::-1]
        