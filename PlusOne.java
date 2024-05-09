class Solution {
    public int[] plusOne(int[] digits) {
        for (int i = digits.length-1; i>=0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            // else, if its 9
            digits[i] = 0;
        }
    
    // if all numbers inside array == 9 (such as [9, 9, 9, 9])
    digits = new int[digits.length+1];  // make it one time longer
    digits[0] = 1;                      // MSB == 1
    return digits;
    }

}
