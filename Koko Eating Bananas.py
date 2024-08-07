class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        res=r

        while l<=r:
            k=(l+r)//2
            hours=0
            for p in piles:
                hours+=math.ceil(p/k)   # rounding up
            if hours<=h:                # ate too slow
                res=min(res,k)
                r=k-1                   # reset pointer
            else:
                l=k+1
        return res
