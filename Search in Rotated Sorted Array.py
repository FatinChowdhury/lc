class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l<=r:
            k=(l+r)//2
            if target not in nums:
                return -1
            if target==nums[k]:
                return k
            if nums[l] <= nums[k]:
                if target>nums[k] or target < nums[l]:
                    l=k+1
                else:
                    r=k-1
            else:
                if target < nums[k] or target > nums[r]:
                    r=k-1
                else:
                    l=k+1

            # initial approach
            # if the number at middle is greater than target
            # move the left index to position mid + 1
            # elif number is smaller than target
            # move right index to position mid - 1
            # return nums[l]
            # if target not in nums then return -1
