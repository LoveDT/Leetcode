class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        if (k <= 0) return {};
        if (k == 1) return nums;
        vector<int> result;
        deque<int> helper;
        for (int i = 0; i < nums.size(); i++) {
            if (helper.empty()) {
                helper.push_back(nums[i]);
                continue;
            }
            if ((i >= k) && (nums[i - k] == helper.front())) {
                helper.pop_front();
            }
            while (!helper.empty() && helper.back() < nums[i]) {
                helper.pop_back();
            }
            helper.push_back(nums[i]);
            if (i >= k - 1) {
                result.push_back(helper.front());
            }
        }
        return result;
    }
};



