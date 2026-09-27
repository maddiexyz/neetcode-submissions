class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        xor=n
        for i in range(n):
            print(xor, i, nums[i])
            xor^= i^nums[i]
        return xor