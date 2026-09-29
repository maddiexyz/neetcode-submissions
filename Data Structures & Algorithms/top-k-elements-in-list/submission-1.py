class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = Counter(nums)
        res=sorted(h,key=h.get,reverse=True)
        return res[:k]