class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int> > helper;
        for (int i = 0; i < m; i++) {
            vector<int> level;
            helper.push_back(level);
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) {
                    helper[i].push_back(grid[i][j]);
                }
                else if (i == 0) {
                    helper[i].push_back(helper[i][j - 1] + grid[i][j]);
                }
                else if (j == 0) {
                    helper[i].push_back(helper[i - 1][j] + grid[i][j]);
                }
                else {
                    helper[i].push_back(min(helper[i - 1][j], helper[i][j - 1]) + grid[i][j]);
                }
            }
        }
        return helper[m - 1][n - 1];
    }
};