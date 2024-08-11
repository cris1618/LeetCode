#include <stack>
#include <unordered_map>
#include <string>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        unordered_map<char, char> mapping = {{')', '('}, {'}', '{'}, {']', '['}};
        
        for (char& c : s) {
            if (mapping.find(c) != mapping.end()) {
                char top_element = !stack.empty() ? stack.top() : '#';
                stack.pop();
                if (top_element != mapping[c]) {
                    return false;
                }
            } else {
                stack.push(c);
            }
        }
        
        return stack.empty();
    }
};
