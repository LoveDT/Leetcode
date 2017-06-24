/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == NULL || head->next == NULL){
            return head;
        }
        ListNode* prevnode = nullptr; 
        ListNode* nextnode;
        ListNode* cur = head;
        while (cur!=NULL){
            nextnode = cur->next;
            cur->next = prevnode;
            prevnode = cur;
            cur = nextnode;
        }
        return prevnode;
    }
};