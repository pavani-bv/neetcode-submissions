class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        left = nums[0]
        right = len(nums)-1
        sum = 0
        while left <= right:
            sum += self.nums[left] + self.nums[right]
            left += 1
            right -=1
    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)