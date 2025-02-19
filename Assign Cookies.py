class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # initial approach (brute force): iterate through every element in s[] and if s[j] >= g[i] then
        # either pop then append to a separate list (which we are going to return its length) or we could simply
        # increment a variable by 1
        # children=0
        # for i in range(len(sorted_G)-1)
        #   for j in range(len(sorted_S)-1)
        #       if s[j]>=g[i] then children+=1
        # but sort the s,g array

        sorted_S = sorted(s)
        sorted_G = sorted(g)
        i=j=0

        while i<len(sorted_G) and j<len(sorted_S):
            if sorted_S[j]>=sorted_G[i]:
                i+=1
            j+=1
        return i
        
