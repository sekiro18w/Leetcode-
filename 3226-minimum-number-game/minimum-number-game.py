class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        turn='A'
        stacc=[]
        for i in range(len(nums)):
            mini=nums.index(min(nums))
            if turn=='A':
                stacc.append(nums[mini])
                turn='B'
            else:
                turn='A'
                x=stacc.pop()
                stacc.append(nums[mini])
                stacc.append(x)
            nums[mini]=101
        return stacc