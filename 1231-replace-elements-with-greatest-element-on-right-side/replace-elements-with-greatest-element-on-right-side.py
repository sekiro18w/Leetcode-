class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        prefix=[arr[-1]]
        for i in range(len(arr)-1,0,-1):
            prefix.append(max(prefix[-1],arr[i]))
        return prefix[::-1][:-1]+[-1]
        