class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        '''
        l at beginning, r from beginning to end
        no result, increment l, start r from incremented l position
        '''
        res = []
        l=0
        for r in range(l, len(numbers)):
            if numbers[l] + numbers[r] != target:
                r += 1
            elif numbers[l] + numbers[r] != target:
                l += 1
                r = l
            elif target == 0:
                res.append(l+1)
                res.append(r+1)
            else:
                res.append(l+1)
                res.append(r+1)
        return res
