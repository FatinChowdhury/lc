class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sum(nums) if we have [3, 0, 1] would be 4
        # sum(range(len(nums)+1)) would be
        # sum(nums) where nums is [0, 1, 2, 3], so 6
        # then the substraction returns 2, missing number
        return sum(range(len(nums)+1))-sum(nums)
