class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        s = list(set(nums))
        s.sort()
        res=1
        i=0
        for j in range(1,len(s)):
            if s[j]==s[j-1]+1:
                res=max(res,j-i+1)
            else:
                i=j
        return res