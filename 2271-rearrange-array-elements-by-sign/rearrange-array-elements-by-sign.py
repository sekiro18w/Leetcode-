class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        pos=[i for i in nums if i>0]
        neg=[i for i in nums if i<0]
        nums=[]
        for i in range(len(pos)):
            nums.append(pos[i])
            nums.append(neg[i])
        return nums
        