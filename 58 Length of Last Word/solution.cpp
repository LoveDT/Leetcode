class Solution {
public:
    int lengthOfLastWord(string s) {
        string result="";
        int leng = s.size();
        for (int i=leng-1;i>=0;i--){
            if (s[i]!=' ')
                result+=s[i];
            else if (result.size()!=0)
                break;
        }
        return result.size();
    }
};