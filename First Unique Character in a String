class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        count = defaultdict(int)

        for c in s:
            count[c] += 1       # increment the position
        
        for i, c in enumerate(s):
            if count[c] == 1:   # if character at a particular index occurs once
                return i        # return it
        return -1
