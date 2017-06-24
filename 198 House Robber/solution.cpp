class Solution {
public:
    int rob(vector<int>& nums) {
        int odd=0;
        int even=0;
        for (int i=0;i<nums.size();i++){
            if (i%2)
                odd = max(odd+nums[i],even);
            else
                even = max(odd,even+nums[i]);
        }
        return max(odd,even);
    }
};