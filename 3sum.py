class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):        # index and value
            if i > 0 and a == nums[i-1]:    
            # i > 0 meaning not 1st value in input array
            # a == nums[i-1] meaning same value as before
                continue
            
            # solving 2sum
            l,r = i+1, len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r-=1
                elif threeSum < 0:
                    l+=1
                else: 
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    # [-2, -2, 0, 0, 2, 2]
        return res
