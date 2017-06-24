class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> result;
        if (numRows==0)
            return result;
        vector<int> helper;
        for (int i=0;i<numRows;i++){
            vector<int> tmp = helper;
            helper.push_back(1);
            for (int j=1;j<i;j++)
                helper[j] = (tmp[j-1]+tmp[j]);
            result.push_back(helper);
        }
        return result;
    }
};