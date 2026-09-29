class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        left = [1]*l
        right = [1]*l
        for i in range(1,l):
            left[i]=left[i-1]*nums[i-1]
            right[l-i-1] = right[l-i]*nums[l-i]
        res=[x*y for x,y in zip(left,right)]
        return res
