class Solution {
public:
    bool isPalindrome(int x) {
        queue<int> helper;
        int tmp = x;
        while (tmp>0){
            int digit = tmp%10;
            helper.push(digit);
            tmp = tmp/10;
        }
        int result = 0;
        int len = helper.size();
        for (int i=0;i<len;i++){
            int revdig = helper.front();
            helper.pop();
            result = result*10+revdig;
        }
        return result==x;
    }
};