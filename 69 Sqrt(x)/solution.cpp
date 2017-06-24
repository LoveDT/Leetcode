class Solution {
public:
    int mySqrt(int x) {
        if (x==0)
            return 0;
        long helper = 0,result = 0;
        while ((result+1)*(result+1)<=x){
            helper = 1;
            while ((result+helper)*(result+helper)<=x){
                helper = helper*2;
            }
            result+=helper/2;
        }
        return result;
    }
};