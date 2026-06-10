class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best_max = 0
        count = 0
        for num in nums:
            if num == 1:
                count+=1
                best_max = max(best_max, count)
            else:
                count = 0
        return best_max

        