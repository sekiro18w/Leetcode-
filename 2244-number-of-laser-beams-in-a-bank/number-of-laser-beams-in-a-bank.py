class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans=0
        for i in range(len(bank)):
            c=0
            for j in range(i+1,len(bank)):
                if '1' in bank[j]:
                    c=bank[j].count('1')
                    break
            ans+=bank[i].count('1')*c
        return ans