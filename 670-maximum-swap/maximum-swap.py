class Solution:
    def maximumSwap(self, num: int) -> int:
        k=[int(i) for i in str(num)]
        x=list(k)
        dic={}
        for i in range(len(k)):
            if k[i] not in dic:
                dic[k[i]]=[]
            dic[k[i]].append(i)
        k.sort(reverse=True)
        for i in range(len(k)):
            if k[i]!=x[i]:
                x[i],x[dic[k[i]][-1]]=x[dic[k[i]][-1]],x[i]
                break
        return int(''.join([str(i) for i in x]))