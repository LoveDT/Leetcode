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
    bool isSymmetric(TreeNode* root) {
        if (root==NULL)
            return true;
        return rechelper(root->left,root->right);
    }
    bool rechelper(TreeNode* left,TreeNode* right){
        if (left==NULL&&right==NULL)
            return true;
        if (left==NULL||right==NULL)
            return false;
        if (left->val!=right->val)
            return false;
        return rechelper(left->left,right->right)&&rechelper(left->right,right->left);
    }
};