class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for num in nums:
            if num in h:
                h[num]+=1
            else:
                h[num]=1
        res=sorted(h,key=h.get,reverse=True)
        return res[:k]