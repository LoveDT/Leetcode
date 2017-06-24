class Solution {
public:
    /**
     * @param s: A string s
     * @param dict: A dictionary of words dict
     */
    bool wordBreak(string s, unordered_set<string> &dict) {
        // write your code here
        vector<bool> result;
        result.push_back(true);
        for (int i = 1; i < s.size() + 1; i++) {
            result.push_back(false);
        }
        int maxlen = 0;
        for (auto it = dict.begin(); it != dict.end(); ++it) {
            string tmp(*it);
            if (tmp.size() >= maxlen) {
                maxlen = tmp.size();
            }
        }
        for (int i = 1; i < result.size(); i++) {
            int start = max(i - maxlen, 0);
            for (int j = start; j< i; j++) {
                if (result[j]) {
                    string tmp = string(s, j, i - j);
                    if (dict.find(tmp) != dict.end()) {
                        result[i] = true;
                        break;
                    }
                }
            }
        }
        return result.back();
    }
};
