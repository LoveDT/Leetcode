class Solution {
public:
    int climbStairs(int n) {
        int prev = 1,cur = 2,next = 0;
        if (n<3)
            next = n;
        else{
            for (int i=3;i<=n;i++){
                next = prev+cur;
                prev = cur;
                cur = next;
            }
        }
        return next;
    }
};