/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        return height(root)>=0;
    }
    int height(TreeNode* root){
        if (root==NULL)
            return 0;
        int lh = height(root->left);
        int rh = height(root->right);
        return (lh>=0&&rh>=0&&abs(lh-rh)<=1)?max(lh,rh)+1:-1;
    }
};