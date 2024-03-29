class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        '''
        l at beginning, r from beginning to end
        no result, increment l, start r from incremented l position
        '''
        res = []
        l=0
        r = len(numbers) - 1
        while l < r:
            totalSum = numbers[l] + numbers[r]

            if totalSum > target:
                r -= 1
            elif totalSum < target:
                l += 1
            else:
                return [l+1,r+1]
        return []
