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
    TreeNode* invertTree(TreeNode* root) {
        if (!root)
            return NULL;
        queue<TreeNode*> resultseq;
        resultseq.push(root);
        while (!resultseq.empty()){
            TreeNode *helper = resultseq.front();
            resultseq.pop();
            TreeNode *tmp = helper->left;
            helper->left = helper->right;
            helper->right = tmp;
            if (helper->left)
                resultseq.push(helper->left);
            if (helper->right)
                resultseq.push(helper->right);
        }
        return root;
    }
};