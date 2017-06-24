class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> result;
        result.push_back(1);
        for (int i=0;i<rowIndex;i++){
            vector<int> tmp = result;
            for (int j=1;j<=i;j++){
                result[j] = tmp[j-1]+tmp[j];
            }
            result.push_back(1);
        }
        return result;
    }
};