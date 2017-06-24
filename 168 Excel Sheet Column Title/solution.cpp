class Solution {
public:
    string convertToTitle(int n) {
        string result = "";
        int tmp = n;
        int count = 0;
        while (tmp>=1){
            count++;
            tmp = (tmp-1)/26;
        }
        for (int i=0;i<count;i++){
            result+=('A'+((n-1)%26));
            n = (n-1)/26;
        }
        string strresult = "";
        int len = result.size();
        for (int i=len-1;i>=0;i--){
            strresult+=(result[i]);
        }
        return strresult;
    }
};