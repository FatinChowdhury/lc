class Solution:
    def romanToInt(self, s: str) -> int:
        
        rom_val = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}

        int_val = 0
        for i in range(len(s)):           # if I is at position before V or X,
                                            # if X is at position before L or C,
                                            # if C is at position before D or M,
            if i+1 < len(s) and rom_val[s[i]] < rom_val[s[i+1]]:
                int_val -= rom_val[s[i]]
            else:
                int_val += rom_val[s[i]]
        return int_val
            
