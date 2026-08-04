class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mi=min(nums)
        ma=max(nums)
        # s=0
        # for i in range(mi,ma+1):
        #     s+=i
        # return [s-sum(nums)]
        s=[]
        r=[]
        for i in range(mi,ma+1):
            s.append(i)
        l=(ma-mi)+1
        for i in range(l):
            if s[i] not in nums:
                r.append(s[i])
        return r
            