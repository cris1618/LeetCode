#include <iostream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

class Solution {
public:
    int lengthOfLastWord(const std::string& s) {
        stringstream ss(s);
        string word;
        vector<std::string> words;

        while (ss >> word) {
            words.push_back(word);
        }

        return words.empty() ? 0 : words.back().length();
    }
};


