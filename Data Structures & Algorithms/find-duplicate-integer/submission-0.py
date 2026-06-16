class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = Counter(nums)
        for i, c in enumerate(nums):
            if count[c]>=2:
                return c