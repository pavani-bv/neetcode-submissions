class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = 1
        dec = 1
        best = 1
        for i in range(len(nums) -1):
            if nums[i+1] > nums[i]:
                inc += 1
                dec = 1
            elif nums[i+1] < nums[i]:
                dec += 1
                inc = 1
            else:
                inc = 1
                dec = 1
            best = max(best,inc,dec)
        return best