class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size()==0)
            return 0;
        if (nums.size()==1)
            return 1;
        int leng = nums.size();
        int i=1,j=1;
        while (i<leng){
            if (nums[i]!=nums[i-1]){
                nums[j] = nums[i];
                j++;
            }
            i++;
        }
        return j;
    }
};