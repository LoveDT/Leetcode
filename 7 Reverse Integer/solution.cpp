class Solution {
public:
    int reverse(int x) {
        long result = 0;
        int rem = 0;
        long tmp = abs(x);
        while (tmp!=0){
            rem = tmp%10;
            tmp = tmp/10;
            result = result*10+rem;
        }
        if (result!=(int)result)
            return 0;
        return (x>0)?result:(-1*result);
    }
};