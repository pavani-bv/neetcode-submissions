class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        values = [x for x in nums if x==val]
        non_values = [x for x in nums if x!=val]
        nums[:] = non_values
        return len(non_values)