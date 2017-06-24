class Solution {
public:
    vector<int> grayCode(int n) {
        if (n < 0) {
            return {};
        }
        vector<int> result;
        int upper = 1 << n;
        for (int i = 0; i < upper; i++) {
            result.push_back((i >> 1) ^ i);
        }
        return result;
        
    }
};