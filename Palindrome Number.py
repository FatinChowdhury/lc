class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x) # int -> str
        n = x[::-1] # getting reverse of x
        if x == n:
            return True
        return False
