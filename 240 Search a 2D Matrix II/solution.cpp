class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (target < matrix[0][0]) return false;
        int row = matrix.size();
        int col = matrix[0].size();
        int cur_row = row - 1, cur_col = 0;
        while (cur_row >= 0 && cur_col < col) {
            if (matrix[cur_row][cur_col] == target)
                return true;
            else if (matrix[cur_row][cur_col] < target)
                cur_col++;
            else
                cur_row--;
        }
        return false;
    }
};



