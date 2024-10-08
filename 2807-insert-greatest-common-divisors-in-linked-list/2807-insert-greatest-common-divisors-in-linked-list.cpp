/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        
            
        
        if(head->next == nullptr) return head;
        
        ListNode* node1 = head;
        ListNode* node2 = head->next;
        
        while(node2 != nullptr){
            int gcd_value = gcd(node1->val, node2->val);
            ListNode* gcd_node = new ListNode(gcd_value);
            
            node1->next = gcd_node;
            gcd_node->next = node2;
            
            node1 = node2;
            node2 = node2->next;
        }
            
        
        return head;
    }
    private:
        
        int gcd(int a, int b){
            while(b != 0){
                int temp = b;
                b = a%b;
                a = temp;
            
            }
          return a;      
        }
    
};