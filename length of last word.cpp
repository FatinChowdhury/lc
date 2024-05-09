class Solution {
public:
    int lengthOfLastWord(string s) {
        
        int length = 0;
        bool boolean = false;

        for (int i = s.length() - 1; i >= 0; i--) {
            if (s[i] != ' ') {
                boolean = true;
                length++;
            }
            else if (boolean) {
                break;
            }
        }
        return length;
    }
};
