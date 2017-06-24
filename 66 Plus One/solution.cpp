class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int quo = 1;
        for (int i = digits.size()-1;i>=0;i--){
            int tmp = quo;
            quo = (digits[i]+tmp)/10;
            digits[i] = (digits[i]+tmp)%10;
        }
        if (quo==1)
            digits.insert(digits.begin(),1);
        return digits;
    }
};