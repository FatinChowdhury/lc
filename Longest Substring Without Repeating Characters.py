class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r, max_len = 0, 0, 0
        count = Counter()
        
        while r < len(s):
            count[s[r]]+=1

            # in case of duplicate:
            while count[s[r]] > 1:
                # restart count of beginning of substr
                count[s[l]]-=1        
                l+=1
        
            max_len = max(max_len, r-l+1)

            r+=1
        return max_len
