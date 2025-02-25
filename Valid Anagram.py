class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = defaultdict(list)
        count = [0] * 26
        count2 = [0] * 26
        
        for c in s:
            count[ord(c)-ord("a")]+=1
        
        for c1 in t:
            count2[ord(c1)-ord("a")]+=1
        
        if count == count2:
            return True
        else:
            return False
