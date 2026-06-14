class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        nums = [x for row in grid for x in row]
        count = Counter(nums)
        repeated = 0
        missing = 0
        for i in range(1,len(nums)+1):
            if count[i] == 2:
                repeated = i
            elif count[i] == 0:
                missing = i
        return [repeated, missing]
        



