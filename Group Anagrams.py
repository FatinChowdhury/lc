class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) 

        for s in strs:
            count = [0] * 26            # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1   # a will be 0 cuz ord("a") - ord("a") = 0
                                                # += 1 because we are counting how many chars we have
            res[tuple(count)].append(s)
            
        return res.values()
