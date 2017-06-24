class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n==0)
            return false;
        int result = 0;
        while (n!=1){
            result = n%2;
            n = n/2;
            if (result)
                return false;
        }
        return true;
    }
};