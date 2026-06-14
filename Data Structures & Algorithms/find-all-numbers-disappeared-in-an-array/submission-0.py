class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums1 = set(nums)
        seen = [] 
        for num in range(1, len(nums)+1):
            if num not in nums1:
                seen.append(num)
        return seen
