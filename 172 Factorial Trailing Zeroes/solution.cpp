class Solution {
public:
    int trailingZeroes(int n) {
        int count = 1;
        while (pow(5,count)<=n)
            count++;
        int result = 0;
        for (int i=1;i<count;i++){
            result+=n/(pow(5,i));
        }
        return result;
    }
};