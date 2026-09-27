class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        longest = 0
        h = {}
        for end, char in enumerate(s):
            if char in h and h[char] >= start:
                start = h[char] + 1
            longest = max(longest, end - start + 1)
            h[char] = end
        return longest