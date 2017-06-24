class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int ct1 = m-1,ct2 = n-1,act = m+n-1;
        while (ct1>=0&&ct2>=0){
            if (nums1[ct1]>=nums2[ct2]){
                nums1[act] = nums1[ct1];
                ct1--;
            }
            else{
                nums1[act] = nums2[ct2];
                ct2--;
            }
            act--;
        }
        while (ct1>=0){
            nums1[act] = nums1[ct1];
            ct1--;
            act--;
        }
        while (ct2>=0){
            nums1[act] = nums2[ct2];
            ct2--;
            act--;
        }
    }
};