#include <cmath>
#include <climits>
#include <vector>
#include <string>

class Solution {
public:
    string nearestPalindromic(string n) {
        int len = n.size();
        int i = len % 2 == 0 ? len / 2 - 1 : len / 2;
        long long firstHalf = stoll(n.substr(0, i + 1));

        vector<long long> possibilities;
        possibilities.push_back(halfToPalindrome(firstHalf, len % 2 == 0));
        possibilities.push_back(halfToPalindrome(firstHalf + 1, len % 2 == 0));
        possibilities.push_back(halfToPalindrome(firstHalf - 1, len % 2 == 0));
        possibilities.push_back((long long)pow10(len - 1) - 1);
        possibilities.push_back((long long)pow10(len) + 1);

        long long diff = LLONG_MAX, res = 0, nl = stoll(n);
        for (auto cand : possibilities) {
            if (cand == nl) continue;
            if (abs(cand - nl) < diff) {
                diff = abs(cand - nl);
                res = cand;
            } else if (abs(cand - nl) == diff) {
                res = min(res, cand);
            }
        }

        return to_string(res);
    }

private:
    long long halfToPalindrome(long long left, bool even) {
        long long res = left;
        if (!even) left = left / 10;
        while (left > 0) {
            res = res * 10 + left % 10;
            left /= 10;
        }
        return res;
    }

    long long pow10(int exp) {
        long long result = 1;
        for (int i = 0; i < exp; i++) {
            result *= 10;
        }
        return result;
    }
};
