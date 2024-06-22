class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # [1,2,3,4,5,6,7,8,9,10], target = 15
        # l,r=0,1
        # while l < r:
        #     remaining = target - numbers[r]
        #     if remaining == numbers[l]:
        #         return [numbers[l], numbers[r]]
        #     if remaining not in numbers:
        #         r+=1
        #     if remaining != numbers[l]:
        #         l+=1

        l,r = 0,len(numbers)-1
        while l < r:
            curSum = numbers[r] + numbers[l]

            if curSum < target:
                l+=1
            elif curSum > target:
                r-=1
            else:
                return [l + 1, r + 1]
